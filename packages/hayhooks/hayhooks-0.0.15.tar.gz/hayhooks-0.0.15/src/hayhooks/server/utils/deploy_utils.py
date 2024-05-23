from fastapi import HTTPException
from fastapi.responses import JSONResponse


from hayhooks.server.pipelines import registry
from hayhooks.server.pipelines.models import (
    PipelineDefinition,
    get_request_model,
    get_response_model,
    convert_component_output,
)


def deploy_pipeline_def(app, pipeline_def: PipelineDefinition):
    try:
        pipe = registry.add(pipeline_def.name, pipeline_def.source_code)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=f"{e}") from e

    PipelineRunRequest = get_request_model(pipeline_def.name, pipe.inputs())
    PipelineRunResponse = get_response_model(pipeline_def.name, pipe.outputs())

    # There's no way in FastAPI to define the type of the request body other than annotating
    # the endpoint handler. We have to ignore the type here to make FastAPI happy while
    # silencing static type checkers (that would have good reasons to trigger!).
    async def pipeline_run(pipeline_run_req: PipelineRunRequest) -> JSONResponse:  # type: ignore
        result = pipe.run(data=pipeline_run_req.dict())
        final_output = {}
        for component_name, output in result.items():
            final_output[component_name] = convert_component_output(output)

        return JSONResponse(PipelineRunResponse(**final_output).model_dump(), status_code=200)

    app.add_api_route(
        path=f"/{pipeline_def.name}",
        endpoint=pipeline_run,
        methods=["POST"],
        name=pipeline_def.name,
        response_model=PipelineRunResponse,
        tags=["pipelines"],
    )
    app.openapi_schema = None
    app.setup()

    return {"name": pipeline_def.name}

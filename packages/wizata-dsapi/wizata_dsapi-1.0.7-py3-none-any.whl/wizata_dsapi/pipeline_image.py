from .api_dto import ApiDto


class PipelineImage(ApiDto):

    def __init__(self,
                 pipeline_image_id: str = None):
        self.pipeline_image_id = pipeline_image_id
        self.files = {}

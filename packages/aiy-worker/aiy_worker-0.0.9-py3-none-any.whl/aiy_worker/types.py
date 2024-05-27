
from enum import Enum
from typing import List

class PayloadErrorLocation:
    line: int
    column: int
    def __init__(self, location: dict):
        self.line = location['line']
        self.column = location['column']

class PayloadError:
    message: str
    locations: List[PayloadErrorLocation]
    path: List[str]

    def __init__(self, error: dict):
        self.message = error['message']
        self.locations = [PayloadErrorLocation(i) for i in error['locations']]
        self.path = error['path']

class Text2ImageProps:
    def __init__(self, props: dict) -> None:
        self.prompt = props.get('prompt')
        self.negative_prompt = props.get('negativePrompt')
        self.seed = props.get('seed')
        self.width = props.get('width')
        self.height = props.get('height')
        self.n_steps = props.get('nSteps')
        self.ip_adapter_image_url = props.get('ipAdapterImageUrl')

class CannyProps:
    def __init__(self, props: dict) -> None:
        self.image_url = props.get('imageUrl')

class TaskKind(Enum):
    TEXT_TO_IMAGE = 1
    CANNY = 2

class Task:
    def __init__(self, data: dict):
        if data is None:
            return
        subscribe_task: dict = data.get('subscribeTasks')
        if subscribe_task:
            self.id = subscribe_task.get('id')
            self.text2Image = None
            if subscribe_task.get('text2Image'):
                self.text2Image = Text2ImageProps(subscribe_task.get('text2Image'))
            self.canny = None
            if subscribe_task.get('canny'):
                self.canny = CannyProps(subscribe_task.get('canny'))

    @property
    def kind(self):
        if self.text2Image is not None:
            return TaskKind.TEXT_TO_IMAGE
        if self.canny is not None:
            return TaskKind.CANNY
        return None

class Payload:
    def __init__(self, payload: dict) -> None:
        self.errors = [PayloadError(i) for i in payload.get('errors', [])]
        self.task = Task(payload.get('data', {}))


class WsData:
    type: str
    id: str
    def __init__(self, data: dict) -> None:
        self.type = data.get('type')
        self.id = data.get('id')
        self.payload = Payload(data.get('payload'))

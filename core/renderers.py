from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        custom_data = {
            "message": None,
            "status": None,
            "data": None,
            "error": None,
        }
        response = renderer_context.get("response")
        message = response.context_data.get('message') if type(response.context_data) is dict else None
        custom_data["status"] = response.status_code
        custom_data["message"] = message
        if response.status_code >= 400:
            custom_data["error"] = data
        else:
            custom_data["data"] = data
        return super().render(custom_data, accepted_media_type, renderer_context)

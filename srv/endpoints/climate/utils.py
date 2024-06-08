from drf_yasg.inspectors import SwaggerAutoSchema

class CustomAutoSchema(SwaggerAutoSchema):
    def get_operation(self, operation_keys):
        operation = super().get_operation(operation_keys)
        # Customize the operation object as needed here
        return operation
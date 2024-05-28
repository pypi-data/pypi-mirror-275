from ._baseclass import BaseClass

class SwaggerParser(BaseClass):
    def __init__(self, ptjsonlib: object):
        self.ptjsonlib: object = ptjsonlib

    def convert(self, args) -> list:
        json_content = self.load_json(args.input)
        root: dict = self.ptjsonlib.create_node_object("webApi", properties={"name": json_content.get("info").get("title"), "webApiType": "webApiTypeRest", "description": json_content.get("info").get("description")})
        nodes_list = [root]

        for path, methods in json_content["paths"].items():
            endpoint_node: dict = self.ptjsonlib.create_node_object("webApiEndpoint", parent=root["key"], properties={"name": path, "url": path})
            nodes_list.append(endpoint_node)

            for method, details in methods.items():
                method_node = self.ptjsonlib.create_node_object("webApiMethod", parent=endpoint_node["key"], properties={
                    "name": method.upper(),
                    "webHttpMethod": f"webHttpMethod{method.capitalize()}",
                    "description": details.get("summary")
                })
                nodes_list.append(method_node)

                for parameter in details.get("parameters"):
                    parameter_type: dict = parameter.get('type')

                    parameter_node = self.ptjsonlib.create_node_object("webInput", parent=method_node["key"], properties={
                    "name": parameter["name"],
                    "description": parameter.get("description"),
                    "webInputType": f"webInputType{parameter_type.capitalize()}" if parameter_type is not None else None
                })
                    nodes_list.append(parameter_node)

        return nodes_list
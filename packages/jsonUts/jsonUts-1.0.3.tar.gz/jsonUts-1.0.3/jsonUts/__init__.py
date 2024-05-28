version = '1.0.3'



class JsonData:
    original_keys = []
    keys = []

    def toJson(self,original_keys=False):
        jsonData = {}
        for k in self.keys:
            my_key = k if not original_keys else self.original_keys[self.keys.index(k)]
            if  isinstance(getattr(self,k), JsonData):
                jsonData[my_key] = getattr(self,k).toJson()
            elif isinstance(getattr(self,k), list):
                jsonData[my_key] = self.list_parse(getattr(self,k))
            else:
                jsonData[my_key] = getattr(self,k)
        return jsonData
    
    
    def list_parse(self,data:list):
        lista_out = []
        for item in data:
            if  isinstance(item, JsonData):
                lista_out.append(item.toJson())
            elif isinstance(item, list):
                lista_out.append(self.list_parse(item))
            else:
                lista_out.append(item)
        return lista_out


            
    def __repr__(self) -> str:
        return f'<JsonData>'


def adjustKey(key,trim_keys=True,lower=False,char_space='_'):
    val = key if not trim_keys else key.strip().replace(' ', char_space)
    val = val if not lower else val.lower()
    return val


def jsonToObj(json_data,trim_keys=True,lower_keys=False,char_space='_'):
    
    if isinstance(json_data, dict) :
        keys,new_keys = [],[]
        obj = JsonData()

        for key in json_data.keys():
            new_key = adjustKey(key,trim_keys,lower_keys,char_space)
            keys.append(key)
            new_keys.append(new_key)

            setattr(obj,new_key,jsonToObj(json_data[key],trim_keys,lower_keys,char_space))

        obj.original_keys = keys
        obj.keys = new_keys
        return obj

    elif isinstance(json_data, list):
        lista=[]
        for item in json_data:
            lista.append(jsonToObj(item,trim_keys,lower_keys,char_space))
        return lista
    else:
        return json_data








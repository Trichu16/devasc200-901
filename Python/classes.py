class Router:
    '''Router Class'''
    def __init__(self, model, swversion, ip_add):
        '''initialize values'''
        self.model = model
        self.swversion = swversion
        self.ip_add = ip_add
rtr1 = Router('iosV', '15.6.7', '10.10.10.1')

'''page 93'''
print (rtr1.model)
rtr1.desc = 'virtual router'
print (rtr1.desc)
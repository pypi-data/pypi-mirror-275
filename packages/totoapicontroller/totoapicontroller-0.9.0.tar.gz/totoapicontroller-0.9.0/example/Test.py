
from flask import Request
from controller.TotoDelegateDecorator import toto_delegate
from controller.model.ExecutionContext import ExecutionContext
from controller.model.UserContext import UserContext
from example.Config import Config


@toto_delegate(config_class=Config)
def test(request: Request, user_context: UserContext, exec_context: ExecutionContext): 
    
    exec_context.logger.log(exec_context.cid, f"It's working!")
    
    return {"ok": True}
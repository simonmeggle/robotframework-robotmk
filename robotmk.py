import json

from robot.api.deco import not_keyword
import inspect
class robotmk():
    """This is a small supplementary library for *Robotmk*, the Robot Framework integration project for *Checkmk*. 
    
    - Github: https://github.com/simonmeggle/robotframework-robotmk
    - Author: Simon Meggle <simon.meggle@elabit.de>
    - Robotmk: https://www.robotmk.org
    - Checkmk: https://checkmk.com

    = Table of contents = 
    
    - `Purpose`
    - `Installation`
    - `Valid state types`
    - `Importing`
    - `Keywords`

    = Purpose =
    
    The keywords in this library do not have any effect on the Robot Framework XML result; they are only interpreted during the state evaluation on a Checkmk system. 
    
    = Installation = 

    ``pip install  robotframework-robotmk``
    
    = Valid state types = 

    The states are given as Nagios states which are: ``OK, WARNING, CRITICAL, UNKNOWN``.

    = Importing = 

    The Library can be imported without any further arguments. 


    """
    ROBOT_LIBRARY_VERSION = "1.0.3.1"

    @not_keyword
    @staticmethod
    def state2str(state, msg):
        all_stack_frames = inspect.stack()
        caller_stack_frame = all_stack_frames[1]
        caller_name = caller_stack_frame[3]
        data = {
            caller_name: {
                'nagios_state': state, 
                'msg': msg
            }
        }
        #return json.dumps(data).encode('utf-8') 
        return json.dumps(data)

    def __init__(self):
        """This library does not take any arguments."""
        pass

    def add_checkmk_test_state(self, state: str, msg: str):
        """Adds a(nother) state to the Robotmk evaluation stack of the current test.

        Use this keyword if you want to change the state of the *current test*, together with a message. 
        
        This is especially useful if the test result in Checkmk should be ``WARNING`` (this state does not exist in Robot Framework).
        
        Remark: for ``OK`` or ``CRITICAL`` results the same effect can be achieved with the RF keywords ``Fail`` and ``Set Test Message``.

        See `Valid state types` section for information about available state types. 

        Example:

        | Add Checkmk Test State    WARNING    Hello. This test will be WARNING in Checkmk.
        """
        print(self.state2str(state, msg))

    def add_robotmk_message(self, state: str, msg: str):
        """Routes a message and state to the "Robotmk" monitoring service in Checkmk. 

        This keyword allows to generate a message/state about *administrative topics*, *unfilfilled preconditions* etc. (e.g. wrong screen resolution) and route it to the *Robotmk* service in Checkmk. This service gets automatically created once on every monitored Robot host and reports everything the *monitoring admins* should take care for. The E2E check availability will no be affected because it will remain ``OK``. 

        Why should you use this keyword? 
        
        Behind an E2E monitoring check there are often two different groups of interest:
        - The *monitoring admins*: They have to take care about the setup of test machines with Robot Framework, Checkmk, Robotmk, etc. It's their job to ensure that E2E tests have a reliable and stable environment to run.
        - The *application owners*: Their work gets judged on the availability report of the application's E2E check. It should only show application outages which actually occured. Therefore, they get pissed off if something unjustifiably pulls down the measured application availability. (In many cases they also are responsible to write the .robot tests).

        See `Valid state types` section for information about available state types. 

        Example:
        | Add Robotmk Message    WARNING    The user password for FooApp is expiring soon; make sure to change it to keep the test running.
        | Add Robotmk Message    CRITICAL   Invalid screen resolution detected! E2E suite ${SUITE_NAME} may run, but is built for 1024x768. 
        """
        print(self.state2str(state, msg))
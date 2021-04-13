import json
from enum import Enum
from robot.api.deco import not_keyword


class robotmk():
    """This is a supplementary library for *Robotmk* (https://www.robotmk.org), the Robot Framework integration project for *Checkmk* (https://checkmk.com). 
    
    = Table of contents = 

    - `Purpose`
    - `Valid state types`
    - `Importing`
    - `Keywords`

    = Purpose =
    This library contains some keywords which do not have any effect on the test _execution_. 
    
    However, it is useful when using Robotmk to integrate Robot tests into Checkmk. 
    
    The keywords make it possible to enrich Robot's XML result with some additional information which then can be processed on the Checkmk server. 

    = Valid state types = 

    The states are given as Nagios states which are: ``OK, WARNING, CRITICAL, UNKNOWN``.

    = Importing = 

    The Library can be imported without any further arguments. 


    """
    ROBOT_LIBRARY_VERSION = "1.0.2"

    @not_keyword
    @staticmethod
    def state2str(state, msg):
        data = {
            'nagios_state': state, 
            'msg': msg
        }
        #return json.dumps(data).encode('utf-8') 
        return json.dumps(data)

    def __init__(self):
        """This library does not take any arguments."""
        pass

    def add_checkmk_test_state(self, state: str, msg: str):
        """Adds a(nother) Nagios state to the Robotmk evaluation stack. 

        Use this keyword if you want to change the state of the *current test*, together with a message. 
        This is especially useful if the test result in Checkmk should be ``WARNING`` (this state does not exist in Robot Framework).
        
        Remark: for ``OK`` or ``CRITICAL`` results the same effect can be achieved with the RF keywords ``Fail`` and ``Set Test Message``.

        See `Valid state types` section for information about available state types. 

        Example:

        | Add Checkmk Test State    WARNING    Hello. This test will be WARNING in Checkmk.
        """
        print(self.state2str(state, msg))

    def add_checkmk_robotmk_state(self, state: str, msg: str):
        """Adds a state to the "Robotmk" monitoring service in Checkmk. 

        The *"Robotmk" service* in Checkmk gets created once on every monitored Robot host and monitors the basic health of the Robotmk setup on this machine. 
        
        Without this keyword, you would write routines which turn the test/suite state into ``FAIL`` with a message containing the reason. This is bad because it results in a CRITICAL state on Checkmk and pulls down the measured availability.  

        Instead, use this keyword for administrative topics like wrong screen resolution, expiring passwords etc. 
        

        This information will be displayed on the "Robotmk" service; the E2E check will stay ``OK``. 
        See `Valid state types` section for information about available state types. 

        Example:
        | Add Checkmk Robotmk State    WARNING    Notification about expiring password detected on FooApp!
        | Add Checkmk Robotmk State    CRITICAL   The screen resolution is not set properly; E2E suite ${SUITE_NAME} depends on 1024x768. 
        """
        print(self.state2str(state, msg))
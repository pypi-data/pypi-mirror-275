# coding: utf-8

"""
  Copyright (c) 2024 Vipas.AI
 
  All rights reserved. This program and the accompanying materials
  are made available under the terms of a proprietary license which prohibits
  redistribution and use in any form, without the express prior written consent
  of Vipas.AI.
  
  This code is proprietary to Vipas.AI and is protected by copyright and
  other intellectual property laws. You may not modify, reproduce, perform,
  display, create derivative works from, repurpose, or distribute this code or any portion of it
  without the express prior written permission of Vipas.AI.
  
  For more information, contact Vipas.AI at legal@vipas.ai
  
"""  # noqa: E501

ERROR_SUGGESTIONS = {
    401: {
        "suggested_actions": [
            "Verify that you are using the correct VPS authentication token.",
            "Ensure the token has not expired and is still valid.",
            "If you are unsure about your token, please contact support for assistance."
        ]
    },
    404: {
        "suggested_actions": [
            "Verify that model id is correct and valid.",
            "Ensure the model with the model id is being deployed.",
            "If the problem persists, please contact support for assistance."
        ]
    },

}

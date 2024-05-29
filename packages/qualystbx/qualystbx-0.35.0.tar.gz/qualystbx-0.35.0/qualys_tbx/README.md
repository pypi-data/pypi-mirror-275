# Test Release, do not use - QualysTBX - Qualys Toolbox Project
QualysTBX is a Toolbox Project of utilities to interact with Qualys.  The initial tool is Policy Merge.  Other tools will be added as needs arise.

## Qualys tools included in QualysTBX:
1. **Policy Merge** - Merge specific CIDs from an old policy into a new policy.


## [Release Notes](#releasenotes)
Note: See the end of this document for history of [release notes](#releasenotes)
- 0.10.0 - Initial Test Release with Policy Merge Tool.

# Usage Information - qualystbx 
<a name="examples"></a>

## 1) Help Screen.
```text
    TBD    

```

# Quick Start


## Prerequisites Python Module on Ubuntu 22.04
    - Install Python Latest Version, greater than 3.9
    - Requires xmltodict,requests

## Installation
<a name="installation"></a>

### First Time Setup Activity on Ubuntu 22.04
 - TBD

# QualysTBX Activity Diagram
- [![](https://github.com/dg-cafe/qualystbx_img/assets/82658653/72bc4bad-f21e-4e2b-9f73-923ca4212cc2)](https://github.com/dg-cafe/qualystbx_img/assets/82658653/72bc4bad-f21e-4e2b-9f73-923ca4212cc2)

# Policy Merge Tool

Policy Merge is a Policy Comliance Function that merges an old policies CID list into a new Policy.  This is useful when customers want to easily merge in their customizations made to existing policies

## Policy Merge Activity Diagram
- [![](https://github.com/dg-cafe/qualystbx_img/assets/82658653/da783563-9b3c-49dc-bf04-c66f89a27e35)](https://github.com/dg-cafe/qualystbx_img/assets/82658653/da783563-9b3c-49dc-bf04-c66f89a27e35)


## Blueprint
TBD

# Roadmap
```
Capability                    | Target    | Description
----------                    | ------    | -----------
Policy Merge                  | May 2024 | Automate Policy Merge of specific CID's between old and new policy.
Other Tools                   | TBD      | Other Qualys Tools
```

## Application Directories

| Path                                                | Description                                                                                    |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------|
| [user storage dir]                                  | Selected by user at runtime via --storage_dir=[path]                                           |
| [user storage dir]/qualystbx/qtbx_home/             | Directory of Tools Data                                                                        |
| qtbx_home/[tool]                                    | Tool Home Directory                                                                            |
| [tool]/bin                                          | Tool bin directory for customer to host scripts they create.                                   |
| [tool]/cred                                      | TBD                                                                                            |
| [tool]/config                                    | TBD                                                                                            |
| [tool]/log                                       | Logs - Directory of all run logs                                                               |
| [tool]/data                                      | Application Data - Directory containing results of tool execution.                             |


# Logging

Logging fields are pipe delimited with some formatting for raw readability.  You can easily import this data into excel, 
 a database for analysis or link this data to a monitoring system.

| Format                      | Description                                                                                                                              |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| YYYY-MM-DD hh:mm:ss,ms      | UTC Date and Time.  UTC is used to match internal date and time within Qualys data.                                                      |
| Logging Level               | INFO, ERROR, WARNING, etc.  Logging levels can be used for troubleshooting or remote monitoring for ERROR/WARNING log entries.           |
| Module Name: YYYYMMDDHHMMSS | Top Level qetl Application Module Name that is executing, along with date to uniquely identify all log entries associated with that job. |
| User Name                   | Operating System User executing this application.                                                                                        |
| Function Name               | qetl Application Function Executing.                                                                                                     |
| Message                     | qetl Application Messages describing actions, providing data.                                                                            |


# Application Monitoring
- To monitor the application for issues, the logging format includes a logging level.  
- Monitoring for ERROR will help identify issues and tend to the overall health of the applicaiton operation.

# Securing Your Application in the Data Center
Follow your corporate procedures for securing your application.  A key recommendation is to use a password vault
or remote invocation method that passes the credentials at run time so the password isn't stored on the system.

## Password Vault
QualysETL provides options to inject credentials at runtime in memory.

Qualys recommends customers move to a password vault of their choosing to operate this applications credentials.
By creating functions to obtain credentials from your corporations password vault, you can improve 
the security of your application by separating the password from the machine, injecting the credentials at runtime.  

One way customers can do this is through a work load management solution, where the external work load management
system ( Ex. Autosys ) schedules jobs injecting the required credentials to QualysETL application at runtime.  This eliminates
the need to store credentials locally on your system.

If you are unfamiliar with password vaults, here is one example from Hashicorp.
- [Hashicorp Products Vault](https://www.hashicorp.com/products/vault)
- [Hashicorp Getting Started](https://learn.hashicorp.com/tutorials/vault/getting-started-intro?in=vault/getting-started)


## qualystbx
You can execute qualystbx to see options available.  

```bash
(qetl_venv) qualystbx@ubuntu:~/.local/bin$ qualystbx
    
            
```

# License
<a name="license"></a>
[Apache License](http://www.apache.org/licenses/LICENSE-2.0)

    Copyright 2021  David Gregory and Qualys Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

# ChangeLog
<a name="changelog"></a>

```
Version | Date of Change      | Description of Changes
------- | --------------      | ----------------------
0.1.0  | 2024-05-17 10:00 ET | Test release, do not use.
0.10.0  | 2024-05-17 10:00 ET | Test release, do not use.
```

# Release Notes Log
<a name="releasenotes"></a>

- 0.1.0 thru 0.10.0 initial test releases, do not use.

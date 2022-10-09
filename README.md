# Overview
This is a simple set of scripts intended to quickly work through the event assignment based on preferencing for the 
FIRST Chesapeake 22-23 FTC season.  Some of this has to be done quickly so excuse the messs.

## Processes and Flows
Working this out for when I write the code.

### Loading and Error Checking
1. Build a list of event zip codes, cross-referencing the linear distance to each event in miles for later selection.
1. Parse event data into event objects.
1. Parse Team Preference selections into Team objects.  Teams should be unique, but it's possible multiple coaches may 
submit so use the most recent submission and log an error to let everyone know.1.
1. Parse a list of teams that have paid invoices
    1. Generate a list of teams that have paid but not selected a preference.
    1. Generate a list of teams attempting to select preference but did not pay

### Assignment Process
1. Iterate through each event and assigned based on team preferences.
    1. If the number of selections for the event are below capacity, assign all teams to the event.
    2. If the number of selections for the event are above capacity, randomly assign teams that have selected it.
    3. Repeat the above for team second and third preferences for teams not already been assigned an event.
1. Handle Teams not able to be assigned through preference selection.
    1. Iterate through each event:
        1. Build a list of teams within 30 miles of that event and randomly assign teams up to capacity.
        1. Repeat this process for increments of 30 miles until all teams have been assigned or no more event capacity
    is available.
1. Produce a list of any remaining team numbers to be added to the top of a waiting list.

### Other Notes
* Each step should produce a CSV that can either be fed to the email system for each notification, or given to staff for
further action.
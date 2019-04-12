![grab-landing-page](/img/ams.gif)

# Departmental Leave-of-Absence Management System

This project is for the fulfilment of my Final Year Project for BSc Computer Science at Royal Holloway.

## Tech Stack

* **Programming languages** - Python, JavaScript
* **Frameworks** - Django
* **Databases** - PostgreSQL

## Features

* **Three user roles:** Administrator, Requester, Authoriser
* **Creating and viewing leave of absence requests:** The system supports the creation of leave of absence requests by the use of web-based forms. The requester has the ability to set the duration of the absence, provide a statement detailing the reason for the absence, select the leave type and attach a document of any type. Submitted requests can also be viewed to check the provided form information when the request was submitted as well download the documents attached to the form. If a leave of absence request is either approved or declined, the requester can also see the authoriser’s comment provided at the time of the decision.
* **Reusing a leave of absence request:** The system supports the reuse of old leave of absence requests. The requester has the ability to reuse old leave of absence requests regardless whether it is still pending, approved or declined. Reusing an old request results in the creation of a new form with all data such as form fields and documents retained from the reused request.
* **Creating and using a template:** The system supports the creation of templates from old leave of absence requests. The requester has the ability to create, use and delete templates created from an old leave of absence request. 
* **Viewing calendar constraints:** The system provides a list of calendar constraints. The requester can view the dates for which the calendar constraint has been set, as well as the reason provided for the constraint.
* **Exporting leave of absences to external calendars:** The system provides the exporting of leave of absences to external calendars. The requester has the ability to download a calendar file which includes events of all approved leave of absences.
* **Approving and declining leave of absence requests:** The system supports approving and declining leave of absence requests. The authoriser has the ability to view requests, download the provided documents and reach a decision by either approving or declining the request.
* **Emailing completed forms:** The system supports the emailing of approved or declined requests. The authoriser has the ability to provide the addressee’s email address, subject of the email, whether to include the form’s attached document and an additional message. The sending of the form is handled by the system’s emailing service, so no email account information needs to be provided for the feature to work.
* **Searching and filtering leave of absence requests:** The system supports the searching and filtering of leave of absence requests. The system user is able to filter requests by ‘All’, ‘Pending’, ‘Approved’ and ‘Declined’. In addition to that, searching allows input of multiple words and will match words or numbers contained in the requests table columns.
* **Receiving of email notifications:** The system supports automatic emailing. Depending on the system user’s role, an automatic email notification is sent out by the system notifying of a new leave of absence submission or a reached decision. 

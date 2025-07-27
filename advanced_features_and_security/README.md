\# README.md (Permissions Setup)



\## Custom Permissions

Defined in the `Article` model:

\- `can\_view`: View articles

\- `can\_create`: Create new articles

\- `can\_edit`: Edit existing articles

\- `can\_delete`: Delete articles



\## Groups Configuration

\- \*\*Viewers\*\*: Assigned `can\_view`

\- \*\*Editors\*\*: Assigned `can\_view`, `can\_create`, `can\_edit`

\- \*\*Admins\*\*: Assigned all four permissions



\## Views Permission Checks

\- `view\_articles`: requires `can\_view`

\- `create\_article`: requires `can\_create`

\- `edit\_article`: requires `can\_edit`

\- `delete\_article`: requires `can\_delete`



\## Testing

Create users via admin panel, assign to groups, and try accessing the URLs to verify enforcement.




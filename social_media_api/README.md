\# Social Media API



\## 📌 Overview

This project is a \*\*Social Media API\*\* built with \*\*Django\*\* and \*\*Django REST Framework (DRF)\*\*.  

The first milestone sets up the project environment, configures authentication, and creates the initial custom user model.  



---



\## 🚀 Features Implemented

\- Django project setup (`social\_media\_api`)

\- Custom user model with:

&nbsp; - `bio`

&nbsp; - `profile\_picture`

&nbsp; - `followers` (self-referencing `ManyToManyField`, non-symmetrical)

\- Token-based authentication using \*\*DRF authtoken\*\*

\- Endpoints for:

&nbsp; - \*\*Register\*\* (`/api/accounts/register/`)

&nbsp; - \*\*Login\*\* (`/api/accounts/login/`)

&nbsp; - \*\*Profile management\*\* (`/api/accounts/profile/`)



---



\## ⚙️ Installation \& Setup



1\. \*\*Clone the repository\*\*

&nbsp;  ```bash

&nbsp;  git clone https://github.com/<your-username>/Alx\_DjangoLearnLab.git

&nbsp;  cd Alx\_DjangoLearnLab




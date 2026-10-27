# OWASP ZAP Analysis Report

## 1. Objective

The objective of this assessment is to evaluate a locally hosted Flask web application using OWASP ZAP, identify potential security issues, test security controls, and document remediation recommendations.

## 2. Testing Environment

* **Operating System:** Kali Linux
* **Web Application:** Python Flask
* **Security Testing Tool:** OWASP ZAP 2.17.0
* **Target URL:** `http://127.0.0.1:5000/`
* **Scope:** Testing was restricted to the locally hosted application.

## 3. Initial Scan Findings

### Finding 1: Absence of Anti-CSRF Tokens

* **Risk reported by ZAP:** Medium
* **Confidence:** Low
* **Location:** `/login`
* **Evidence:** The initial scan identified a form that appeared to lack an anti-CSRF token.
* **Remediation:** Flask-WTF CSRF protection was implemented, and a CSRF token was added to the form.
* **Verification:** A POST request without a CSRF token was rejected with HTTP 400 Bad Request.
* **Status:** The missing-token test passed. Additional verification of all state-changing forms and routes is required.

### Finding 2: Server Version Information Disclosure

* **Risk reported by ZAP:** Low
* **Confidence:** High
* **Location:** `/sitemap.xml`
* **Initial Evidence:** The response exposed `Werkzeug/3.1.9 Python/3.13.12` in the Server header.
* **Remediation:** The application launcher was configured to filter the Server header.
* **Verification:** A later response showed `Server: waitress` rather than the earlier Werkzeug/Python version string.
* **Status:** The earlier version details were no longer exposed in the inspected response. The Server header still identifies Waitress, so complete server identification removal has not been verified.

### Finding 3: Authentication Request Identified

* **Risk reported by ZAP:** Informational
* **Location:** `/login`
* **Evidence:** ZAP identified authentication-related parameters, including username and password.
* **Interpretation:** This alert identifies an authentication request. It does not, by itself, establish a vulnerability.
* **Status:** Documented.

## 4. Subsequent Scan Findings

The subsequent ZAP scan displayed the following alerts:

### Finding 4: Cookie Without SameSite Attribute

* **Risk:** Confirm the exact risk displayed by ZAP.
* **Evidence:** ZAP reported a cookie without a SameSite attribute.
* **Potential Impact:** Depending on how the cookie is used, the absence of this attribute may increase exposure to certain cross-site request scenarios.
* **Recommendation:** Inspect the cookie's Set-Cookie header and configure an appropriate SameSite policy if required.
* **Status:** Requires further verification.

### Finding 5: Session Management Response Identified

* **Risk:** Record the risk displayed by ZAP.
* **Evidence:** ZAP identified a response associated with session management.
* **Interpretation:** This alert alone does not confirm a vulnerability.
* **Recommendation:** Review the session cookie and verify appropriate security attributes and session handling.
* **Status:** Requires review.

### Finding 6: User-Controlled HTML Element Attribute

* **Risk:** Record the risk displayed by ZAP.
* **Evidence:** ZAP identified an HTML element attribute that may contain user-controlled data.
* **Potential Impact:** If user-controlled data is inserted into HTML unsafely, it may create an injection risk.
* **Recommendation:** Inspect the affected URL and evidence, and verify that user-controlled values are appropriately escaped or validated.
* **Status:** Requires further investigation.

## 5. Authentication and Session Testing

The following application functions were tested manually:

* User registration
* User login
* Dashboard access after login
* Logout
* Rejection of a POST request without a CSRF token

The application functions worked during the manual registration and login test. The missing-token CSRF test returned HTTP 400 Bad Request.

## 6. Limitations

* Testing was limited to the local lab application.
* Automated scanner alerts may include informational findings and false positives.
* The subsequent scan findings have not all been independently verified.
* The assessment does not establish that the application is free from vulnerabilities.
* Further testing is needed to assess authorization controls, input handling, session security, and other relevant OWASP Top 10 risks.

## 7. Conclusion

OWASP ZAP identified several security-related findings during testing. CSRF protection was implemented and tested against a POST request without a token. The earlier Werkzeug/Python version disclosure was reduced, although the Server header still identified Waitress.

Other findings require further review before they can be classified as confirmed vulnerabilities. The results demonstrate the process of identifying, testing, documenting, and recommending improvements to web application security.

## 8. Recommended Next Steps

1. Record the exact risk, URL, and evidence for each subsequent ZAP alert.
2. Verify the SameSite attribute of the session cookie.
3. Investigate the user-controlled HTML attribute finding.
4. Review session handling and access control.
5. Complete the vulnerability report and remediation recommendations.
6. Prepare the demo walkthrough and organize the final project repository.


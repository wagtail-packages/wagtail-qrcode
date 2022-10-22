# Setup mail-hog

For testing email sending locally run `make mail`

This will execute a docker command to start up mail hog and add some configuration to wagtail.

The mail-hog web interface will be available at `http://localhost:8025` **Before testing this feature** you may need to stop and start the django development server

## Test sending an email with attached QR code

With the test app set up: create a QRCode page and on the QRcode tab complete the field to send an email you can access the QR code sample page in the admin and add an email address before saving the page.

The email will show up in mail hog.

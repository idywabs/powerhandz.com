<?php
    // Added input sanitizing to prevent injection

    // Only process POST reqeusts.
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Get the form fields and remove whitespace.
        $fname = trim($_POST["formFirstName"]);
        $lname = trim($_POST["formLastName"]);
        $position = trim($_POST["formPosition"]);
        $email = filter_var(trim($_POST["formMail"]), FILTER_SANITIZE_EMAIL);
        $phone = trim($_POST["formPhone"]);
        $website = trim($_POST["formPortfolio"]);
        $age = trim($_POST["formAge"]);
        $city = trim($_POST["formCity"]);
        $startdate = trim($_POST["formStartdate"]);
        $message = trim($_POST["formApplication"]);

        $name = $fname . ' ' . $lname;
        $name = str_replace(array("\r","\n"),array(" "," "),$name);

        // Check that data was sent to the mailer.
        if ( empty($name) OR empty($message) OR !filter_var($email, FILTER_VALIDATE_EMAIL)) {
            // Set a 400 (bad request) response code and exit.
            http_response_code(400);
            echo "Oops! There was a problem with your submission. Please complete the form and try again.";
            exit;
        }

        // Set the recipient email address.
        // FIXME: Update this to your desired email address.
        $recipient = "you@yourmail.com";

        // Set the email subject.
        $subject = "New Job Application";
        
        // Build the email content.
        $email_content = "Name: $name\n";
        $email_content .= "Position: $position\n\n";
        $email_content .= "Email: $email\n\n";
        $email_content .= "Phone Number: $phone\n\n";
        $email_content .= "Website: $website\n\n";
        $email_content .= "Age: $age\n\n";
        $email_content .= "City: $city\n\n";
        $email_content .= "Start Date: $startdate\n\n";
        $email_content .= "Message:\n$message\n";

        // Build the email headers.
        $email_headers = "From: $name <$email>";

        // Send the email.
        if (mail($recipient, $subject, $email_content, $email_headers)) {
            // Set a 200 (okay) response code.
            http_response_code(200);
            echo "Thank You! Your message has been sent.";
        } else {
            // Set a 500 (internal server error) response code.
            http_response_code(500);
            echo "Oops! Something went wrong and we couldn't send your message.";
        }

    } else {
        // Not a POST request, set a 403 (forbidden) response code.
        http_response_code(403);
        echo "There was a problem with your submission, please try again.";
    }

?>

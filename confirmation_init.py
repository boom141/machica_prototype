import os
class Email_confirmation:
	def __init__(self,data):
		self.data = data

	def generate_html(self):
		 return f"""
		   			<html>
					<head>
					<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
					<link rel="stylesheet" href="{os.path.join('static', 'confirm.css')}">
					<title></title>
					<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
					<meta name="viewport" content="width=device-width, initial-scale=1">
					<meta http-equiv="X-UA-Compatible" content="IE=edge" />
					<body style="margin: 0 !important; padding: 0 !important; background-color: #eeeeee;" bgcolor="#eeeeee">
					<table border="0" cellpadding="0" cellspacing="0" width="100%">
					<tr>
					<td align="center" style="background-color: #eeeeee;" bgcolor="#eeeeee">
					<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
					<tr>
					<td align="center" valign="top" style="font-size:0; padding: 35px;" bgcolor="#003A33">
					<div style="display:inline-block; max-width:50%; min-width:100px; vertical-align:top; width:100%;">
					<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;">
					<tr>
					<td align="left" valign="top" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 36px; font-weight: 800; line-height: 48px;" class="mobile-center">
					<h1 style="font-size: 1.2rem; font-weight: 800; margin: 0; color: #ffffff;">Mahica Dental clinic</h1>
					</td>
					</tr>
					</table>
					</div>
					<div style="display:inline-block; max-width:50%; min-width:100px; vertical-align:top; width:100%;" class="mobile-hide">
					<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:300px;">
					<tr>
					<td align="right" valign="middle" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; line-height: 48px;">
					<table cellspacing="0" cellpadding="0" border="0" align="right">
					<tr>
					<td style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: 400; line-height: 24px;"> <a href="#" target="_blank" style="color: #ffffff; text-decoration: none;"><img src="https://i.pinimg.com/564x/e7/b6/52/e7b652b5be3ef0ddcb90e1226049aa67.jpg" width="30" height="30" style="display: block; border: 0px;" /></a> </td>
					</tr>
					</table>
					</td>
					</tr>
					</table>
					</div>
					</td>
					</tr>
					<tr>
					<td align="center" style="padding: 35px 35px 20px 35px; background-color: #ffffff;" bgcolor="#ffffff">
					<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
					<tr>
					<td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 25px;"> <img src="https://img.icons8.com/carbon-copy/100/000000/checked-checkbox.png" width="125" height="120" style="display: block; border: 0px;" /><br>
					<h2 style="font-size: 30px; font-weight: 800; line-height: 36px; color: #009886; margin: 0;">Your {self.data['transaction_type']} is confirmed! </h2>
					</td>
					</tr>
					<tr>
					</tr>
					<tr>
					<td align="left" style="padding-top: 20px;">
					<table cellspacing="0" cellpadding="0" border="0" width="100%">
					<tr>
					<td width="75%" align="left" bgcolor="#eeeeee" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px;"> {self.data['transaction_type']} Reference ID </td>
					<td width="25%" align="left" bgcolor="#eeeeee" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px;">{self.data['reference_id']}</td>
					</tr>
					<tr>
					<td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 15px 10px 5px 10px;">{self.data['entity_type']}</td>
					<td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 15px 10px 5px 10px;">sample price</td>
					</tr>
					<tr>
					<td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 5px 10px;"> Payment method </td>
					<td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 5px 10px;"> Over the counter </td>
					</tr>
					</table>
					</td>
					</tr>
					<tr>
					<td align="left" style="padding-top: 20px;">
					<table cellspacing="0" cellpadding="0" border="0" width="100%">
					<tr>
					<td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> TOTAL </td>
					<td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 800; line-height: 24px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> sample total </td>
					</tr>
					</table>
					</td>
					</tr>
					</table>
					</td>
					</tr>
					<tr>
					<td align="center" height="100%" valign="top" width="100%" style="padding: 0 35px 35px 35px; background-color: #ffffff;" bgcolor="#ffffff">
					<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:660px;">
					</table>
					</td>
					</tr>
					<tr>
					</tr>
					<tr>
					<td align="center" style="padding: 35px; background-color: #ffffff;" bgcolor="#ffffff">
					<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
					<tr>
					<td align="center"> <img src="https://i.pinimg.com/564x/75/8d/cc/758dccad44bd73e2a5f7106024b27fef.jpg" width="37" height="37" style="display: block; border: 0px;" /> </td>
					</tr>
					<tr>
					<td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 24px; padding: 5px 0 10px 0;">
					<p style="font-size: 14px; font-weight: 800; line-height: 18px; color: #333333;">Unit #1, G/F Aspiras Building,<br> Consolacion Street </p>
					</td>
					</tr>
					<tr>
					<td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 24px;">
					<p style="font-size: 14px; font-weight: 400; line-height: 20px; color: #777777;"> If you didn't create an account using this email address, please ignore this email or <a href="#" target="_blank" style="color: #777777;">unsusbscribe</a>. </p>
					</td>
					</tr>
					</table>
					</td>
					</tr>
					</table>
					</td>
					</tr>
					</table>
					</body>
					</html> 
				"""
	
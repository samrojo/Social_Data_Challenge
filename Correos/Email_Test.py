from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def Send_mail(email, gender, ID, mail):

    # me == my email address
    # you == recipient's email address
    me = ""
    you = email

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Seguimiento cuestionario 'Burnout'"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = ""
    html = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="https://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
    <!--[if gte mso 9]><xml>
    <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
    </xml><![endif]-->
    <title>Correo</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0 ">
    <meta name="format-detection" content="telephone=no">
    <!--[if !mso]><!-->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800" rel="stylesheet">
    <!--<![endif]-->
    <style type="text/css">
    body {{
        margin: 0 !important;
        padding: 0 !important;
        -webkit-text-size-adjust: 100% !important;
        -ms-text-size-adjust: 100% !important;
        -webkit-font-smoothing: antialiased !important;
    }}
    img {{
        border: 0 !important;
        outline: none !important;
    }}
    p {{
        Margin: 0px !important;
        Padding: 0px !important;
    }}
    table {{
        border-collapse: collapse;
        mso-table-lspace: 0px;
        mso-table-rspace: 0px;
    }}
    td, a, span {{
        border-collapse: collapse;
        mso-line-height-rule: exactly;
    }}
    .ExternalClass * {{
        line-height: 100%;
    }}
    .em_defaultlink a {{
        color: inherit !important;
        text-decoration: none !important;
    }}
    span.MsoHyperlink {{
        mso-style-priority: 99;
        color: inherit;
    }}
    span.MsoHyperlinkFollowed {{
        mso-style-priority: 99;
        color: inherit;
    }}
     @media only screen and (min-width:481px) and (max-width:699px) {{
    .em_main_table {{
        width: 100% !important;
    }}
    .em_wrapper {{
        width: 100% !important;
    }}
    .em_hide {{
        display: none !important;
    }}
    .em_img {{
        width: 100% !important;
        height: auto !important;
    }}
    .em_h20 {{
        height: 20px !important;
    }}
    .em_padd {{
        padding: 20px 10px !important;
    }}
    }}
    @media screen and (max-width: 480px) {{
    .em_main_table {{
        width: 100% !important;
    }}
    .em_wrapper {{
        width: 100% !important;
    }}
    .em_hide {{
        display: none !important;
    }}
    .em_img {{
        width: 100% !important;
        height: auto !important;
    }}
    .em_h20 {{
        height: 20px !important;
    }}
    .em_padd {{
        padding: 20px 10px !important;
    }}
    .em_text1 {{
        font-size: 16px !important;
        line-height: 24px !important;
    }}
    u + .em_body .em_full_wrap {{
        width: 100% !important;
        width: 100vw !important;
    }}
    }}
    </style>
    </head>
    
    <body class="em_body" style="margin:0px; padding:0px;" bgcolor="#efefef">
    <table class="em_full_wrap" valign="top" width="100%" cellspacing="0" cellpadding="0" border="0" bgcolor="#efefef" align="center">
      <tbody><tr>
        <td valign="top" align="center"><table class="em_main_table" style="width:700px;" width="700" cellspacing="0" cellpadding="0" border="0" align="center">
            <!--Header section-->
            <tbody>
    <!--	<tr>
              <td style="padding:15px;" class="em_padd" valign="top" bgcolor="#f6f7f8" align="center"><table width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
                  <tbody><tr>
                    <td style="font-family:'Open Sans', Arial, sans-serif; font-size:12px; line-height:15px; color:#0d1121;" valign="top" align="center">Correo de PRUEBA <a href="#" target="_blank" style="color:#0d1121; text-decoration:underline;">View Online</a></td>
                  </tr>
                </tbody></table></td>
            </tr> -->
    
            <!--//Header section-->
            <!--Banner section-->
            <tr>
              <td valign="top" align="center"><table width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
                  <tbody><tr>
                    <td valign="top" align="center">
                        <img class="em_img" alt="BURNOUT CHALLENGE" style="display:block; font-family:Arial, sans-serif; font-size:30px; line-height:34px; color:#000000; max-width:700px;" src="" width="700" border="0">
                    </td>
                  </tr>
                </tbody></table></td>
            </tr>
            <!--//Banner section-->
            <!--Content Text Section-->
            <tr>
                <td style="padding:35px 70px 30px;" class="em_padd" valign="top" bgcolor="#efefef" align="center">
                    <table width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
                        <tbody>
                            <tr>
                                <td style="font-family:'Open Sans', Arial, sans-serif; font-size:26px; line-height:30px; color:#0d1121;" valign="top" align="center">Gracias por tu confianza</td>
                             </tr>
                            <tr>
                                <td style="font-size:0px; line-height:0px; height:15px;" height="15">&nbsp;</td>
                            <!--—this is space of 15px to separate two paragraphs ---->
                            </tr>
                            <tr>
                                <td style="font-family:'Open Sans', Arial, sans-serif; font-size:18px; line-height:22px; color:#0d1121; letter-spacing:2px; padding-bottom:12px;" valign="top" align="justify">
                                    <!--—This is paragraph 2 of font size 18px and #fbeb59 font color with a line spacing of 15px -->
   
   
                                </td>
                            </tr>
                            <tr>
                                <td class="em_h20" style="font-size:0px; line-height:0px; height:25px;" height="25">&nbsp;</td>
                                <!--—this is space of 25px to separate two paragraphs ---->
                            </tr>
                            <tr>
                                <td style="font-family:'Open Sans', Arial, sans-serif; font-size:18px; line-height:22px; color:#0d1121; text-transform:uppercase; letter-spacing:2px; padding-bottom:12px;" valign="top" align="center">
                                    <!--—This is paragraph 3 of font size 18px and #fbeb59 font color with a line spacing of 25px and Uppercase-->




                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
    
            <!--//Content Text Section-->
            <!--Footer Section-->
            <tr>
                <td style="padding:38px 30px;" class="em_padd" valign="top" bgcolor="#f6f7f8" align="center"><table width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
                    <tbody>
                        <tr>
                            <td style="padding-bottom:16px;" valign="top" align="center">
                                <table cellspacing="0" cellpadding="0" border="0" align="center">
                                    <tbody><tr>
                                      <td valign="top" align="center"><a href="https://www.facebook.com/Burnout-Challenge-110204960744122" target="_blank" style="text-decoration:none;">
                                        <img src="https://img2.freepng.es/20180511/ssq/kisspng-facebook-inc-logo-computer-icons-facebook-messen-5af555fbaefdc9.9980502215260277717168.jpg" alt="fb" style="display:block; font-family:Arial, sans-serif; font-size:14px; line-height:14px; color:#ffffff; max-width:26px;" width="26" border="0" height="26"></a>
                                      </td>
                                    </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        <tr>
                            <td style="font-family:'Open Sans', Arial, sans-serif; font-size:11px; line-height:18px; color:#999999;" valign="top" align="center">
                            <!--<a href="#" target="_blank" style="color:#999999; text-decoration:underline;">PRIVACY STATEMENT</a>
                            | <a href="#" target="_blank" style="color:#999999; text-decoration:underline;">TERMS OF SERVICE</a>-->
                            <br>
                              2020 Burnout Challenge<br>
                              Este correo forma parte del seguimiento del cuestionario <strong><a href="https://forms.gle/fd3t19mtMTEzDmPy8" target="_blank" style="text-decoration:none; color:#999999;">Burnout en médicos y enfermeros - MX</a></strong>, si usted no contestó este cuestionario favor de eliminar e ignorar este correo. <a href="#" target="_blank" style="text-decoration:none; color:#999999;"></a>
                            </td>
                        </tr>
                    </tbody></table>
                </td>
            </tr>
            <tr>
              <td class="em_hide" style="line-height:1px;min-width:700px;background-color:#ffffff;"><!--<img alt="" src="http://imgfz.com/i/6HtNsbE.jpeg" style="max-height:1px; min-height:1px; display:block; width:700px; min-width:700px;" width="700" border="0" height="1">--</td>
            </tr>
          </tbody></table></td>
      </tr>
    </tbody></table>
    <div class="em_hide" style="white-space: nowrap; display: none; font-size:0px; line-height:0px;">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</div>
    </body></html>
    """.format(ID,gender)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)


    mail.sendmail(me, you, msg.as_string())
#######################################################################################################################

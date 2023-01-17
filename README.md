# WP-brute-force
## It is a simple brute force python script for webpages
  
  To run this script first of all you have to install requests python module
 
    pip install requests
    
   If you don't have any idea about pip and how to install that <a href="https://pypi.org/project/pip/">click here.</a>
   
   When you run this script it will ask you to input a URL,make sure that you're giving correct URL because sometimes a file may redirect to another file.
   For example look at the following image.In this image the page is redirected to another page.
    
 ![Picsart_23-01-17_17-14-40-866](https://user-images.githubusercontent.com/120016997/212894946-d8c3a440-6d48-4711-9f42-a2d09c42004a.png)
  
   And second page is the one which has form data in the request.
 
 ![Picsart_23-01-17_17-16-15-351](https://user-images.githubusercontent.com/120016997/212895611-d3c132da-d09c-49cd-b0c8-ea4fbf1876b9.png)

   So you have to give correct URL like in following image.

   ![urllink](https://user-images.githubusercontent.com/120016997/212898770-21c8cc49-da0a-40f6-b546-5ce8299d3d69.png)

   In the second option you have to give method.In this example the method is POST.
   
   ![Picsart_23-01-17_17-17-43-238](https://user-images.githubusercontent.com/120016997/212899255-86004c58-9706-42c9-b60f-bb4dfbbb1641.png)
  
   ![Picsart_23-01-17_17-13-09-689 (copy 1)](https://user-images.githubusercontent.com/120016997/212899529-33493741-93d3-4e72-8cfc-06c8a1534f00.png)
   
   In the third option you have to give request parameters name(first two parameters should be username and password parameters).
   
   ![Picsart_23-01-17_17-19-53-098](https://user-images.githubusercontent.com/120016997/212900402-729a7135-59bf-4374-a328-9c209187843b.png)

   ![Picsart_23-01-17_17-10-42-350](https://user-images.githubusercontent.com/120016997/212900261-a83cfa02-4b5b-4721-b841-b355b15eeaca.png)
   
   In the fourth option you should give error message which appears when the login fails.
   
   ![Picsart_23-01-17_17-09-33-489](https://user-images.githubusercontent.com/120016997/212901272-8a25609d-2e5a-41b8-8df6-13f59ffe34b4.png)
   
   For next few options you have to give values for request parameters.
   
   1) You can give wordlists for both username and password parameters.
  
   ![Picsart_23-01-17_17-05-36-439](https://user-images.githubusercontent.com/120016997/212901962-318034eb-eb12-4254-855a-eca682ad5087.png)

   2) Or you can give wordlist for username parameter and string value for password parameter. 
   
   ![Picsart_23-01-17_17-02-47-054](https://user-images.githubusercontent.com/120016997/212902415-1d617fa1-1e9e-4881-aade-0f49a68f366c.png)

   3) Or you can give string value for username and wordlist for password parameter.
   
   ![Picsart_23-01-17_17-04-16-215](https://user-images.githubusercontent.com/120016997/212902629-5189f706-6915-433c-88f9-cc4dbc10f828.png)

   Sometimes you could get "password found" output for all the given values,it occurs when the tool fails to detect the given error in the fourth         option.Still you can find the correct username and password through content length.
   
   ![Picsart_23-01-17_16-57-58-867](https://user-images.githubusercontent.com/120016997/212904293-e202ff8e-6d8a-43de-9714-a38d1d484dce.png)


   <b>Thank You ...!</b>
   

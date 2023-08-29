# Digitari Technical Test Backend - Yonatan Shahar
## Description

<font size=3>This API matches phone numbers to speakers of the main language in their respective countries.
It accepts formats such as “+44141555555” or “44 555 512 34” etc. and returns:
* The Phone Number provided
* The Calling Code
* User
  * Country Details 
  * The default language 
  * The country name 
  * The name of the country in the user's default language 
  * The region 
  * The flag URL

## Usage

To execute the Test Backend API, run the main_api.py file.

To test the small API, the follow country codes were used:
* Martinique +596
* Colombia +57
* Zimbabwe +263
* United States +1
* Hungary +36 
* Czech Republic +420  


## Approach Description
### Research
* I thoroughly reviewed the documentation for the restcountries API, which can be found at https://github.com/apilayer/restcountries.
* I employed the Postman application to inspect the values retrieved from the API.

### Design
I created a process flow diagram to enhance my understanding of the requirements.
You can access the diagram in the project document folder:
[Link](https://github.com/yonatan-moa/yonshar_digirati_01/blob/fc85641c53122fa3b9570634028d228736086892/docs/Code_test_diagram.pdf).

### Implementation
1. I developed a main function to drive the overall process.
2. I designed a function that retrieves users based on the languages they speak.
3. I established a class called User with an __init__ method to initialize instance variables such as name as a string and langs as a list.
4. I created a list of User instances, each initialized with a name and a list of languages spoken by the user.
5. I provided an input prompt to enter the phone number.
6. I extracted the country code and country number from the entered phone number.
7. A GET request was sent to the endpoint located at https://restcountries.com/v2/callingcode/. I then converted the response to JSON format.
8. From the JSON data, I extracted the required fields/values.
9. Using the language data in ISO 639-1 format, I retrieved the corresponding user based on the response JSON data. If no language match was found, I assigned the user with the most languages in their list.
10. The required information was outputted.

## Issues
* Initially, I used string slicing to extract the phone country code, which led to validation issues. I later reconsidered the prototype's scalability and approached it with a more Digitari-focused perspective.
* The current method of task assignment to users through a list is simplistic. For scalability, users should be organized in a relational schema with comprehensive metadata.

## Observations - Suggestions
* I made a conscious decision to exclude a phone number validator in this prototype due to increased complexity.
* For continued development of this small API, validation and unit testing are essential considerations.
* To enhance the API further, gathering more extensive metadata from users, such as their experience, feedback, and resolved number of issues, would be beneficial.
* While I randomly selected a user for assignment, it would be more effective to implement a user selection mechanism that considers the user's language proficiency.

## End Note

I found the task engaging and even experimented with the API by incorporating unique country 
codes such as Martinique and Colombia,
along with other territories.
While I was tempted
to refine the API with comprehensive unit tests and intricate validation techniques,
I decided against it to avoid potential pitfalls,
like the complexities of country-specific codes 
and regional variations that could introduce unnecessary intricacies at this stage.</font>

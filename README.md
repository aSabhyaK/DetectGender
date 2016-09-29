# DetectGender
Detects the gender of a person by analysing their first name

To determine the gender of a person by their first name, two approaches have been considered, and have been given weightages to each of these approaches to maximize the success rate.
 
Approach 1 :
Using the BeautifulSoup library, the method "gender_scraping" parses the top n google results (set to 5) and looks for the occurrence of any of the predefined values present in the array(e.g. female_array = ['female', 'woman', 'girl', 'feminine']) in the top results' URL, the title and the source code and adds different weightage to each of them. 
Two counters - female_counter and male_counter have been recorded throughout.
 
Approach 2 :
A general observation speaks of a majority of female names ending with an 'a' or an 'i'. The method "gender_last_character" adds a specific weight (2) to the female_counter if the name ends with an 'a' or 'i'  and if it doesn't, the male_counter gets incremented.
 
The final result is evaluated by comparing the two counters, the larger of them winning and in case the counters happen to be equal then we say it is an "ambiguous" name.

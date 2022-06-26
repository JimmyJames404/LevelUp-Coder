from leetapi import leetcode
from github import github
from stack import stack



stack_results = stack("https://stackoverflow.com/users/14452043/jimmy-j")
github_results = github("JimmyJames404")
leetcode_results = leetcode("Jimmy_James")


# stack_results = stack("https://stackoverflow.com/users/14102957/marco-perez")
# github_results = github("marco-alberto")
# leetcode_results = leetcode("marco_apc")

# Estimated Stackoverflow points

stack_reputacion = int(stack_results["reputacion"])
stack_reached = int(stack_results["reached"])
stack_answers = int(stack_results["answers"])
stack_questions = int(stack_results["questions"])
stack_points = (stack_reputacion*3 + stack_reached + stack_answers*10 + stack_questions*2)*0.75

# Estimated github points

github_repos = int(github_results["numRepos"])
github_contributions = int(github_results["contributions"])
github_languages_num = len(github_results["languages"])
github_points = github_repos + github_contributions*0.1 + github_languages_num


# Estimated leetcode points
leet_easy = leetcode_results["easy"]
leet_medium = leetcode_results["medium"]
leet_hard = leetcode_results["hard"]
leet_ranking = leetcode_results["ranking"]
leet_points = (leet_easy*4 + leet_medium*8 + leet_hard*10)/leet_ranking*1000000

total_points = stack_points + github_points + leet_points

print("############Resultados Stack #################")
print(stack_results)
print("############Resultados Github #################")
print(github_results)
print("############Resultados Leetcode #################") 
print(leetcode_results) 
print("############Puntos Leetcode #################")
print(leet_points)
print("############Puntos Stack #################")
print(stack_points)
print("############Puntos Github #################")
print(github_points)
print("############Puntos Totales #################")
print(total_points)




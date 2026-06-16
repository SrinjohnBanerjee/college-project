import pandas as pd
from final_features import extract_features, havingat, havingdash, emergencywords, depthhave, numbr, platformabuse, brandassubdirectory, typosquat, ipinurl, httpinurl
df=pd.read_csv(r"the path")
final_features.extract_features(url),
final_features.havingat(url),
final_features.havingdash(url),
final_features.emergencywords(url),
final_features.depthhave(url),
final_features.numbr(url),
final_features.platformabuse(url),
final_features.brandassubdirectory(url),
final_features.typosquat(url),
final_features.ipinurl(url),
final_features.httpinurl(url)

df["url"]=df["new_column_name_of_your_choice"].apply(a function from the above)

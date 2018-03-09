import xml.etree.cElementTree as ET

cse = ET.Element("CustomSearchEngine", id="wmi5btyfcmu", creator="004585795627402740186", language="en", encoding="UTF-8", enable_suggest="true")
title = ET.SubElement(cse, "Title").text ="Hello World"
context = ET.SubElement(cse, "Context")
backGroundLabels = ET.SubElement(context, "BackgroundLabels")
label1 = ET.SubElement(backGroundLabels, "Label", name="_cse_wmi5btyfcmu", mode="FILTER")
label2 = ET.SubElement(backGroundLabels, "Label", name="_cse_exclude_wmi5btyfcmu", mode="ELIMINATE")

lookAndFeel = ET.SubElement(cse, "LookAndFeel", nonprofit="false", element_layout="8", theme="7", custom_theme="true", text_font="Arial, sans-serif", url_length="full", element_branding="show", enable_cse_thumbnail="true", promotion_url_length="full", ads_layout="1")
logo = ET.SubElement(lookAndFeel, "Logo")
colors = ET.SubElement(lookAndFeel, "Colors", url="#008000", background="#FFFFFF", border="#FFFFFF", title="#0000CC", text="#000000", visited="#0000CC", title_hover="#0000CC", title_active="#0000CC")
promotions = ET.SubElement(lookAndFeel, "Promotions", title_color="#0000CC", title_visited_color="#0000CC", url_color="#008000", background_color="#FFFFFF", border_color="#336699", snippet_color="#000000", title_hover_color="#0000CC", title_active_color="#0000CC")
searchControls = ET.SubElement(lookAndFeel, "SearchControls", input_border_color="#D9D9D9", button_border_color="#666666", button_background_color="#CECECE", tab_border_color="#E9E9E9", tab_background_color="#E9E9E9", tab_selected_border_color="#FF9900", tab_selected_background_color="#FFFFFF")
results = ET.SubElement(lookAndFeel, "Results", border_color="#FFFFFF", border_hover_color="#FFFFFF", background_color="#FFFFFF", background_hover_color="#FFFFFF", ads_background_color="#fff7f5", ads_border_color="#FFFFFF")

adSense = ET.SubElement(cse, "AdSense")
entAccount = ET.SubElement(cse, "EnterpriseAccount")
autoComplete = ET.SubElement(cse, "autocomplete_settings")
sort1 = ET.SubElement(cse, "sort_by_key", label="Relevance", key="")
sort2 = ET.SubElement(cse, "sort_by_key", label="Date", key="date")
advanced = ET.SubElement(cse, "cse_advance_settings", enable_speech="true")


tree = ET.ElementTree(cse)
tree.write("filename.xml")
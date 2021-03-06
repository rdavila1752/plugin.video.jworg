# -*- coding: UTF-8 -*-

# for utf-8 see http://www.python.org/dev/peps/pep-0263/

import jw_config
import jw_common

from video import jw_video
from video import jw_sign

from audio import jw_audio
from audio import jw_audio_bible
from audio import jw_audio_music
from audio import jw_audio_drama
from audio import jw_audio_dramatic_reading
from audio import jw_audio_magazine

from program import jw_exec_index
from program import jw_exec_daily_text
from program import jw_exec_news
from program import jw_exec_week_program
from program import jw_exec_activity

from generic import jw_menu

"""
START
"""
# call arguments
params 		 = jw_config.plugin_params

try:
	content_type = params["content_type"][0]
except:
	content_type = "menu" 
	pass

mode = None
try: 	
	mode = params["mode"][0]
except:
	pass


"""
Call router
"""
if content_type == "menu" :
	jw_menu.showMenu()

if content_type == "video" :
	if mode is None :
		jw_video.showVideoIndex(0, "none")

	if mode == "open_video_filter":
		jw_video.showVideoFilter()

	if mode == "open_video_index":
		start = params["start"][0]        
		video_filter = params["video_filter"][0]	#Note: video_filter can be 'none', and it's a valid filter for jw.org !
		jw_video.showVideoIndex(start, video_filter)

	if mode == "open_json_video":
		json_url 	= params["json_url"][0]
		thumb 		= params["thumb"][0]
		jw_video.showVideoJsonUrl(json_url, thumb)

	if mode == "open_sign_index":
		jw_sign.showVideoFilter()

	if mode == "open_sign_video_category":
		url 	= params ["url"][0]
		thumb 	= params ["thumb"][0]
		jw_sign.showVideoCategory(url, thumb)

	if mode == "open_sign_video_category_with_specific_issue":
		url 			= params ["url"][0]
		thumb 			= params ["thumb"][0]
		pub_title_index = params ["pub_title_index"][0]
		jw_sign.showVideoCategorySpecificIssue(url, thumb, pub_title_index)

	if mode == "open_sign_video_category_specific_row":
		url 		= params ["url"][0]
		thumb 		= params ["thumb"][0]
		row_index 	= params ["row_index"][0]		
		jw_sign.showVideoCategorySpecificRow(url, thumb, row_index)

	if mode == "open_sign_video_sel_year":
		url 		= params ["url"][0]
		thumb 		= params ["thumb"][0]
		jw_sign.selYear(url, thumb)

	if mode == "open_sign_video_sel_book":
		url 		= params ["url"][0]
		thumb 		= params ["thumb"][0]
		jw_sign.selBook(url, thumb)		


if content_type == "audio" :
	if mode is None :
		jw_audio.showAudioIndex()

	if mode == "open_bible_index" :
		jw_audio_bible.showAudioBibleIndex()

	if mode == "open_bible_book_index"  :
		book_num = params["book_num"][0]
		jw_audio_bible.showAudioBibleBookJson(book_num)

	if mode == "open_music_index" :
		start = params["start"][0]
		jw_audio_music.showMusicIndex( start)

	if mode == "open_music_json" : 
		json_url = params["json_url"][0]
		jw_audio.showAudioJson(json_url)

	if mode == "open_drama_index" :
		start = params["start"][0]
		jw_audio_drama.showDramaIndex( start)

	if mode == "open_drama_json" : 
		json_url = params["json_url"][0]
		jw_audio.showAudioJson(json_url)

	if mode == "open_dramatic_reading_index": 
		start = params["start"][0]
		jw_audio_dramatic_reading.showDramaticReadingIndex( start)

	if mode == "open_dramatic_reading_json" : 
		json_url = params["json_url"][0]
		jw_audio.showAudioJson(json_url)

	if mode == "open_magazine_index" :
		try: pub_filter = params["pub_filter"][0]
		except : pub_filter = None
		try: year_filter = params["year_filter"][0]
		except : year_filter = None

		if year_filter is None :
			jw_audio_magazine.showMagazineFilterIndex(pub_filter)
		else :
			jw_audio_magazine.showMagazineFilteredIndex(pub_filter, year_filter)

	if mode == "open_magazine_json" :
		json_url = params["json_url"][0]
		jw_audio.showAudioJson(json_url)

	if mode == "play_mp3" :
		url = params["file_url"][0]
		jw_common.playMp3(url)
		

if content_type == "executable" :
	if mode is None : 
		jw_exec_index.showExecIndex()

	if mode == "open_daily_text" : 
		date = params["date"][0]
		jw_exec_daily_text.showDailyText(date)

	if mode == "open_news_index" :
		jw_exec_news.showNewsIndex()

	if mode == "open_news_page" :
		url = params["url"][0]
		jw_exec_news.showNewsPage(url)

	if mode == "open_week_program" :
		date = params["date"][0]
		jw_exec_week_program.showWeekProgram(date)

	if mode == "open_activity_index" :
		jw_exec_activity.showActivityIndex()

	if mode == "open_activity_section" :		
		url = params["url"][0]
		jw_exec_activity.showActivitySection(url)

	if mode == "open_activity_article" :
		url = params["url"][0]
		jw_exec_activity.showArticle(url)



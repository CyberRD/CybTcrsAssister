# -*- coding: utf-8 -*-


class ActivityInfo(object):

    project_name = ""
    loc_project = ""

    loc_activity = ""
    text = ""


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def build_activities(proj_loc_info_dict):

    activities = {}

    for proj_name, proj_info in proj_loc_info_dict.iteritems():

        for activity in proj_info[2]:

            activity_info = ActivityInfo()
            activity_info.project_name = proj_name
            activity_info.loc_project = proj_info[0] # get project locator
            activity_info.loc_activity = proj_info[1] # get activity locator
            activity_info.text = activity

            activities[activity] = activity_info

    return activities

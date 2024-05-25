from os.path import join, dirname

import radiosoma
from ovos_utils import classproperty
from ovos_utils.ocp import MediaType, PlaybackType
from ovos_utils.parse import fuzzy_match
from ovos_utils.process_utils import RuntimeRequirements
from ovos_workshop.decorators.ocp import ocp_search, ocp_featured_media
from ovos_workshop.skills.common_play import OVOSCommonPlaybackSkill


class SomaFMSkill(OVOSCommonPlaybackSkill):

    def __init__(self, *args, **kwargs):
        super().__init__(supported_media=[MediaType.MUSIC, MediaType.RADIO],
                         skill_icon=join(dirname(__file__), "somafm.png"),
                         *args, **kwargs)

    def initialize(self):
        # register with OCP to help classifier pick MediaType.RADIO
        self.register_ocp_keyword(MediaType.RADIO,
                                  "radio_station", [s.title for s in radiosoma.get_stations()])
        self.register_ocp_keyword(MediaType.RADIO,
                                  "radio_streaming_provider",
                                  ["SomaFM", "Soma FM", "Soma"])

    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(internet_before_load=True,
                                   network_before_load=True,
                                   gui_before_load=False,
                                   requires_internet=True,
                                   requires_network=True,
                                   requires_gui=False,
                                   no_internet_fallback=False,
                                   no_network_fallback=False,
                                   no_gui_fallback=True)

    @ocp_featured_media()
    def featured_media(self):
        return [{
            "match_confidence": 90,
            "media_type": MediaType.RADIO,
            "uri": ch.direct_stream,
            "playback": PlaybackType.AUDIO,
            "image": ch.image,
            "bg_image": ch.image,
            "skill_icon": self.skill_icon,
            "title": ch.title,
            "author": "SomaFM",
            "length": 0
        } for ch in radiosoma.get_stations()]

    @ocp_search()
    def ocp_somafm_playlist(self, phrase):
        phrase = self.remove_voc(phrase, "radio")
        if self.voc_match(phrase, "somafm", exact=True):
            yield {
                "match_confidence": 100,
                "media_type": MediaType.RADIO,
                "playlist": self.featured_media(),
                "playback": PlaybackType.AUDIO,
                "skill_icon": self.skill_icon,
                "image": "https://somafm.com/img3/LoneDJsquare400.jpg",
                "bg_image": "https://somafm.com/about/pics/IMG_0974.jpg",
                "title": "SomaFM (All stations)",
                "author": "SomaFM"
            }

    @ocp_search()
    def search_somafm(self, phrase, media_type):
        base_score = 0

        if media_type == MediaType.RADIO:
            base_score += 20
        else:
            base_score -= 30

        if self.voc_match(phrase, "radio"):
            base_score += 10
            phrase = self.remove_voc(phrase, "radio")

        if self.voc_match(phrase, "somafm"):
            base_score += 30  # explicit request
            phrase = self.remove_voc(phrase, "somafm")

        for ch in radiosoma.get_stations():
            score = round(base_score + fuzzy_match(ch.title.lower(), phrase.lower()) * 100)
            if score < 50:
                continue
            print(ch.title, score)
            yield {
                "match_confidence": min(100, score),
                "media_type": MediaType.RADIO,
                "uri": ch.direct_stream,
                "playback": PlaybackType.AUDIO,
                "image": ch.image,
                "bg_image": ch.image,
                "skill_icon": self.skill_icon,
                "title": ch.title,
                "author": "SomaFM",
                "length": 0
            }

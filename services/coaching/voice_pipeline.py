import time
import streamlit as st

class VoicePipeline:
    def __init__(self,llm,tts):
        self.llm = llm
        self.tts = tts
        self.last_spoken_at = 0

    def _get_form_issue(self, exercise, metrics):

        if "issue" in metrics:
            return metrics["issue"]

        if exercise == "Squats":

            depth = metrics.get("depth_status", "N/A")
            back_angle = metrics.get("back_angle", 180)

            if depth == "TOO HIGH":
                return (
                    "The user's squat depth is not enough - "
                    "their knees are not bent enough. "
                    "They should lower their hips more to achieve a proper squat."
                )

            if isinstance(back_angle, (int, float)) and back_angle < 70:
                return (
                    "The user's back is too bent forward during the squat. "
                    "They should straighten their back to avoid injury."
                )

        elif exercise == "Push-ups":

            alignment = metrics.get("body_alignment", "")
            hip_status = metrics.get("hip_status", "")

            if alignment == "Poor Form":
                return (
                    "The user's body alignment is off during the push-up. "
                    "They should keep their body straight from head to heels."
                )

            if hip_status == "SAGGING":
                return (
                    "The user's hips are sagging during the push-up. "
                    "They should engage their core and keep their hips in line with their body."
                )

            if hip_status == "PICKED UP":
                return (
                    "The user's hips are raised too high during the push-up. "
                    "They should lower their hips to maintain a straight line from head to heels."
                )

        elif exercise == "Biceps Curls (Dumbbell)":

            swing = metrics.get("swing_status", "")
            shoulder = metrics.get("shoulder_status", "")

            if swing == "SWINGING":
                return (
                    "The user is swinging their arms during the bicep curl. "
                    "They should keep their elbows close to their torso and avoid using momentum."
                )

            if shoulder == "ELBOW DRIFTING":
                return (
                    "The user's elbows are drifting away from their torso during the bicep curl. "
                    "They should keep their elbows stationary and close to their body."
                )

        elif exercise == "Shoulder Press":

            back_arch = metrics.get("back_arch_status", "")
            extension = metrics.get("extension_status", "")

            if back_arch == "Excessive Arch":
                return (
                    "The user is arching their back too much during the shoulder press. "
                    "They should engage their core and keep their back straight."
                )

            if back_arch == "Slight Arch":
                return (
                    "Slight back arch detected. "
                    "Encourage the user to brace their core and maintain a neutral spine."
                )

        elif exercise == "Lunges":

            balance = metrics.get("balance_status", "")

            if balance == "OFF BALANCE":
                return (
                    "The user is off balance during the lunge. "
                    "They should focus on keeping their weight centered and maintain a stable stance."
                )

        return None
    
    def process_event(self,event, exercise,metrics):
        issue = self._get_form_issue(exercise, metrics)

        now = time.time()

        is_major_issue = event in ["workout_started", "set_completed", "workout_completed"]

        if not is_major_issue:
            if not issue:
                return None

            if now - self.last_spoken_at < 5:
                return None

        text = self.llm.give_feedback(event, issue)
        voice = self.tts.speak(text)

        self.last_spoken_at = now

        return voice, text


def autoplay_audio(audio_bytes):

    if not audio_bytes:
        return

    st.markdown("<style>[data-testid='stAudio'] {display: none;}</style>", unsafe_allow_html=True)

    st.audio(audio_bytes, format="audio/mp3", autoplay=True)    

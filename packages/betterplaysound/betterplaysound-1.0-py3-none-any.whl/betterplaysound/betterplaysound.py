from pygame import mixer, time
import sys
import os
import platform
import subprocess

def get_system():
    """
    Detect the operating system.
    Returns:
        str: The name of the operating system.
    """
    system = platform.system()
    if system == 'Windows':
        return "Windows"
    elif system == 'Darwin':
        return "Mac"
    elif system == 'Linux':
        return "Linux"
    else:
        return "Other"

def playsound(file, volume=0.7):
    """
    Play a sound file with the specified volume using pygame mixer.
    
    Args:
        file (str): Path to the sound file.
        volume (float): Volume level (default is 0.7).
    """
    try:
        mixer.init()
        mixer.music.load(file)
        mixer.music.set_volume(volume)
        mixer.music.play()
        running = True
        while running:
            if not mixer.music.get_busy():
                running = False
            time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing sound: {e}")
    finally:
        mixer.quit()

def sysplay(file):
    """
    Play a sound file using the system's default application.
    
    Args:
        file (str): Path to the sound file.
    """
    system = get_system()
    try:
        if system == "Windows":
            os.system(f'start "" "{file}"')
        elif system == "Linux":
            subprocess.Popen(['xdg-open', file])
        elif system == 'Mac':
            subprocess.Popen(['open', file])
        else:
            print("Unsupported operating system")
    except Exception as e:
        print(f"Error playing sound on system: {e}")

def main():
    """
    Main function to play a sound file from the command line.
    """
    if len(sys.argv) > 1:
        audio_file = sys.argv[1]
        if os.path.exists(audio_file):
            playsound(audio_file)
        else:
            print(f"File {audio_file} does not exist.")
    else:
        print("Usage: betterplaysound <path_to_audio_file>")

if __name__ == "__main__":
    main()

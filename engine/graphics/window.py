import glfw
from OpenGL.GL import *

from engine.core.event_sysyem import *

vertex_source = ""

fragment_source = ""

class Window:
    def __init__(self, event_manager: EventManager):
        self.event_manager = event_manager

        if not glfw.init():
            msg = f"glfw couldn't be initialized"
            event_info = Event(INFO_EVENT, self, msg)
            self.event_manager.dispatch_event(event_info)

            return
        
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.window = glfw.create_window(800, 600, "Title", None, None)
        if not self.window:
            glfw.terminate()

            msg = f"Failed to create a new window"
            event_info = Event(INFO_EVENT, self, msg)
            self.event_manager.dispatch_event(event_info)

            return
        
        glfw.make_context_current(self.window)
        glfw.set_framebuffer_size_callback(self.window, self.framebuffer_callback)

        msg = f"window [{self.window}] created"
        event_info = Event(INFO_EVENT, self, msg)
        self.event_manager.dispatch_event(event_info)

        while(not glfw.window_should_close(self.window)):
            glClearColor(0.2, 0.3, 0.3, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)

            glfw.swap_buffers(self.window)
            glfw.poll_events()

        glfw.terminate()

        msg = f"window [{self.window}] closed"
        event_info = Event(INFO_EVENT, self, msg)
        self.event_manager.dispatch_event(event_info)

        return

    def framebuffer_callback(self, window, width, height):
        glViewport(0, 0, width, height)

        msg = f"window [{self.window}] resized {width, height}"
        event_info = Event(INFO_EVENT, self, msg)
        self.event_manager.dispatch_event(event_info)

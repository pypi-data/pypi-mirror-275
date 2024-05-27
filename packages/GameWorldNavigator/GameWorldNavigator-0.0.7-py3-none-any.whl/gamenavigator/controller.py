from ast import Tuple
from re import I
from typing import Any, Type, Union
from .core import Interface, InterfaceAction as Action, InterfaceStep, Pos, Image
from .game_controller import GameController
from .game_interface_controller import GameInterfaceController

class Controller:
    def __init__(self, game_class: Union[str, None], game_name: str, root_inf: Interface) -> None:
        self.game_controller = GameController(game_class, game_name)
        self.inf_controller = GameInterfaceController(root_inf)
    
    def to_interface(self, inf_name: str) -> None:
        """切换界面

        Args:
            inf_name (str): 想要前往的界面
        """
        target_inf = self.inf_controller.get_interface(inf_name)
        steps = self.inf_controller.to_interface(inf_name)
        
        for step in steps:
            self.__run_inf_step(step)
        
        self.inf_controller.set_current(inf_name)
    
    def __run_inf_step(self, step: InterfaceStep) -> None:
        """运行界面步骤
        
        Args:
            step (InterfaceStep): 界面步骤
        
        """
        for action, arg in step:
            match action:
                case Action.MOUSE_CLICK:
                    if isinstance(arg, tuple):
                        raise TypeError("Invalid mouse click argument")
                    self.__mouse_click(arg)
                case Action.MOUSE_MOVE:
                    if isinstance(arg, tuple):
                        raise TypeError("Invalid mouse click argument")
                    self.__mouse_move(arg)
                case Action.MOUSE_DRAG:
                    if not isinstance(arg, Pos):
                        raise TypeError("Invalid mouse drag argument")
                    self.__mouse_drag(arg)
                case Action.KEYBOARD:
                    if not isinstance(arg, (str, tuple)):
                        raise TypeError("Invalid keyboard argument")
                    self.__keyboard(arg)
    
    def __mouse_click(self, arg: Union[str, Image, Pos]) -> None:
        """鼠标点击

        Args:
            arg (Union[str, Image, Pos]): 要点击的元素,可以是文字,图像,位置

        Raises:
            TypeError: Invalid mouse click argument
        """
        if isinstance(arg, str):
            self.game_controller.click_text(arg, y=5)
        elif isinstance(arg, Image):
            self.game_controller.click_image(arg.cv2_image)
        elif isinstance(arg, Pos):
            self.game_controller.click_pos(arg)
        else:
            raise TypeError("Invalid mouse click argument")
    
    def __mouse_move(self, arg: Union[str, Image, Pos]) -> None:
        """移动鼠标

        Args:
            arg (Union[str, Image, Pos]): 鼠标可以移动到文字,图像,位置
        """
        if isinstance(arg, Image):
            self.game_controller.mouse_move_to(arg.cv2_image, 0.0)
        else:
            self.game_controller.mouse_move_to(arg, 0.0)
    
    def __mouse_drag(self, arg):
        pass
    
    def __keyboard(self, arg: str | tuple) -> None:
        if isinstance(arg, str):
            self.game_controller.down_keyboard_time(arg, 0.0)
        elif isinstance(arg, tuple):
            self.game_controller.down_keyboard_time(*arg)

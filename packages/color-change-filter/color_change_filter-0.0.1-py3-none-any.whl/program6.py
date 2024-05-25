import cv2
import numpy as np


class ColorChanger():
    def select_color(self, img):
        selected_color = None
        clicked = False

        def get_color(event, x, y, flags, param):
            nonlocal selected_color, clicked
            if event == cv2.EVENT_LBUTTONDOWN:
                selected_color = img[y, x]
                clicked = True
                print(f"selected: {selected_color}")

        # 画像を表示してクリックイベントを設定
        cv2.imshow('Select Color', img)
        cv2.setMouseCallback('Select Color', get_color)
        print("Please select a color by clicking on the image.")
        print("Press ESC to finish.")

        while True:
            cv2.imshow('Select Color', img)
            if cv2.waitKey(20) & 0xFF == 27 or clicked:  
                break

        cv2.destroyAllWindows()
        return selected_color if clicked else None
      
    def get_color_at_pixel(self, img, x, y):
        # 画像の範囲外の場合はNoneを返す
        if x < 0 or y < 0 or x >= img.shape[1] or y >= img.shape[0]:
            return None

        selected_color = img[y, x]
        print(f"selected pixel ({x}, {y}) color: {selected_color}")
        return selected_color

    def apply_color_change(self, img, selected_color, target_color):
        selected_color = [selected_color[2], selected_color[1], selected_color[0]]  
        selected_color = np.array(selected_color, dtype=np.float32)
        target_color = np.array(target_color, dtype=np.float32)
        diff_color = target_color - selected_color

        img = img.astype(np.float32) + diff_color
        img = np.clip(img, 0, 255).astype(np.uint8)

        return img

    def select_color_from_hue_circle(self):
        hue_circle = np.zeros((200, 200, 3), dtype=np.uint8)

        for i in range(200):
            for j in range(200):
                angle = np.arctan2(i - 100, j - 100)
                hue = np.degrees(angle) % 360
                saturation = np.sqrt((i - 100) ** 2 + (j - 100) ** 2) / 100.0
                if saturation <= 1.0:
                    hsv = np.uint8([[[hue / 2, saturation * 255, 255]]])  
                    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
                    hue_circle[i, j] = rgb

        selected_color = [0, 0, 0]
        clicked = False

        def get_color(event, x, y, flags, param):
            nonlocal selected_color, clicked
            if event == cv2.EVENT_LBUTTONDOWN:
                selected_color = hue_circle[y, x]
                hsv_selected = cv2.cvtColor(np.uint8([[selected_color]]), cv2.COLOR_BGR2HSV)[0][0]
                clicked = True
                print(f"selected (BGR): {selected_color}")
                print(f"selected (HSV): {hsv_selected}")

        # 色相環を表示してクリックイベントを設定
        cv2.imshow('Hue Circle', hue_circle)
        cv2.setMouseCallback('Hue Circle', get_color)

        while True:
            cv2.imshow('Hue Circle', hue_circle)
            if cv2.waitKey(20) & 0xFF == 27 or clicked:  # ESCキーを押すかクリックされると終了
                break

        cv2.destroyAllWindows()
        return selected_color if clicked else None

    def color_change_GUI(self, image_path,output_path):
        img = cv2.imread(image_path)

        selected_color = self.select_color(img)
        if selected_color is None:
            print("Do not select color. Program will be terminated.")
            return

        target_color = self.select_color_from_hue_circle()
        if target_color is None:
            print("Do not select color. Program will be terminated.")
            return

        result_img = self.apply_color_change(img, selected_color, target_color)

        output_path = output_path
        cv2.imwrite(output_path, result_img)
        cv2.destroyAllWindows()
        print(f"Save at {output_path}")
        
    def color_change_CUI(self, image_path,output_path,x,y,rgb):
        # 画像の読み込み
        img = cv2.imread(image_path)

        # ピクセルを選択して色を取得
        selected_color = self.get_color_at_pixel(img,x,y)

        # 任意の色を入力
        target_color = rgb
        if target_color is None:
            print("Do not select color. Program will be terminated.")
            return
        else:
            target_color = [target_color[2], target_color[1], target_color[0]]

        # 色の変更
        result_img = self.apply_color_change(img, selected_color, target_color)

        # 結果の保存
        output_path = output_path
        cv2.imwrite(output_path, result_img)
        cv2.destroyAllWindows()
        print(f"Save {output_path}")

def main():
    color_changer = ColorChanger()
if __name__ == '__main__':
    main()

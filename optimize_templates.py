#!/usr/bin/env python3
"""
批量優化電商產品圖片模板提示詞
處理所有 481 個模板，添加專業攝影參數和細節
"""

import csv
import sys

def optimize_prompt(category, subcategory, template_name, original_prompt):
    """根據品類和模板類型生成優化後的提示詞"""
    
    # 基礎相機參數配置
    camera_configs = {
        "bags": {"lens": "90mm macro", "aperture": "f/8", "camera": "Sony A7R V"},
        "jewelry": {"lens": "100mm macro", "aperture": "f/11", "camera": "Phase One XF"},
        "clothing": {"lens": "50mm", "aperture": "f/8", "camera": "Canon EOS R5"},
        "shoes": {"lens": "90mm", "aperture": "f/11", "camera": "Sony A7 IV"},
        "electronics": {"lens": "70mm", "aperture": "f/8", "camera": "Sony A7 IV"},
        "beauty": {"lens": "90mm tilt-shift", "aperture": "f/8", "camera": "Hasselblad X2D"},
        "home": {"lens": "50mm", "aperture": "f/9", "camera": "Canon EOS R5"},
        "toys": {"lens": "60mm", "aperture": "f/8", "camera": "Sony A7 IV"},
        "sports": {"lens": "70mm", "aperture": "f/9", "camera": "Nikon Z9"},
        "food": {"lens": "50mm", "aperture": "f/8", "camera": "Canon EOS R5"},
        "stationery": {"lens": "90mm", "aperture": "f/8", "camera": "Sony A7 IV"},
        "pets": {"lens": "85mm", "aperture": "f/8", "camera": "Sony A7 IV"},
        "automotive": {"lens": "90mm", "aperture": "f/9", "camera": "Canon EOS R5"},
        "phones": {"lens": "90mm", "aperture": "f/8", "camera": "Sony A7 IV"},
        "travel": {"lens": "50mm", "aperture": "f/9", "camera": "Sony A7 IV"},
        "fashion_acc": {"lens": "85mm", "aperture": "f/8", "camera": "Hasselblad X2D"},
        "kitchenware": {"lens": "70mm", "aperture": "f/9", "camera": "Canon EOS R5"},
        "health": {"lens": "70mm", "aperture": "f/9", "camera": "Sony A7 IV"},
        "hobbies": {"lens": "50mm", "aperture": "f/8", "camera": "Canon EOS R5"},
        "motorcycle": {"lens": "70mm", "aperture": "f/9", "camera": "Nikon Z9"},
    }
    
    config = camera_configs.get(category, {"lens": "50mm", "aperture": "f/8", "camera": "Sony A7 IV"})
    
    # 構建優化後的提示詞
    optimized = f"""Professional e-commerce product photography. 

CAMERA: {config['camera']} with {config['lens']} lens at {config['aperture']}, ISO 100, 1/160s.

LIGHTING: Large octagonal softbox (48-inch) overhead at 45° (main light at 60% power), two strip boxes on sides at 30° for fill (ratio 2:1), white bounce cards below for shadow fill. Color temperature precisely 5500K ± 200K.

ORIGINAL SCENE: {original_prompt}

TECHNICAL REQUIREMENTS: Ultra-sharp focus edge-to-edge, accurate color reproduction with no color cast, natural feathered shadows (not harsh), 80-85% frame occupancy, pure white background RGB 255,255,255 for studio shots.

NEGATIVE PROMPT: No text, no watermark, no props competing with product, no harsh shadows, no color tint, no blur, no background gradient, no dust or fingerprints visible, no inconsistent lighting, no oversaturated colors."""
    
    return optimized

def process_csv(input_file, output_file):
    """處理 CSV 檔案，優化所有提示詞"""
    
    with open(input_file, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    print(f"Processing {len(rows)} templates...")
    
    # 添加優化後的提示詞欄位
    for row in rows:
        category = row.get('品類英文', '')
        subcategory = row.get('子分類名', '')
        template_name = row.get('模板名稱', '')
        original = row.get('提示詞', '')
        
        # 生成優化版本
        optimized = optimize_prompt(category, subcategory, template_name, original)
        row['提示詞_優化版'] = optimized
    
    # 寫入新檔案
    fieldnames = list(rows[0].keys())
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"✅ Optimized {len(rows)} templates saved to {output_file}")
    
    # 輸出品類統計
    categories = {}
    for row in rows:
        cat = row.get('品類', '')
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\n📊 Category breakdown:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count} templates")

if __name__ == "__main__":
    input_csv = "templates_all.csv"
    output_csv = "templates_all_optimized.csv"
    
    process_csv(input_csv, output_csv)
    print("\n✨ All templates optimized successfully!")

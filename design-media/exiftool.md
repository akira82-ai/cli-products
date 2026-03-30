# ExifTool (`exiftool`)

## 基本信息
- 官方文档：https://exiftool.org/
- 安装方式：`brew install exiftool`
- 开源：是 (Artistic License / GPL-1.0+)
- 平台支持：macOS / Linux / Windows
- 最后验证版本：v13.00

## 核心命令示例
```bash
# 查看图片的所有 EXIF 信息
exiftool photo.jpg

# 删除所有元数据（隐私保护）
exiftool -all= photo.jpg

# 批量修改照片的拍摄日期
exiftool -AllDates="2024:01:15 12:00:00" *.jpg

# 根据拍摄日期重命名文件
exiftool "-filename<CreateDate" -d "%Y-%m-%d_%H-%M-%S%%-c.%%e" *.jpg

# 提取 GPS 坐标信息
exiftool -gpslatitude -gpslongitude photo.jpg
```

## 适用场景
- 查看、编辑和删除照片元数据
- 批量整理照片（按日期重命名/归档）
- 图片隐私保护（上传前移除敏感 EXIF 信息）

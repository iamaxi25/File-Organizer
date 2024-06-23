import os

director_path = r"C:\Users\axi\Downloads"

# Dictionary used for
file_extensions = {
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".tex", ".wpd", ".md", ".wks", ".wps", ".pages"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".xlsm", ".xlt", ".xltx", ".xltm", ".numbers"],
    "Presentations": [".ppt", ".pptx", ".odp", ".key", ".pps", ".ppsx", ".pptm"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".psd", ".heic", ".ico", ".raw",
               ".nef", ".cr2"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a", ".aiff", ".alac", ".amr", ".mid", ".midi"],
    "Video": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg", ".m4v", ".3gp", ".3g2", ".rm",
              ".vob"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".dmg", ".tgz", ".cab", ".z", ".lz",
                   ".lzma"],
    "Executables": [".exe", ".bat", ".sh", ".jar", ".msi", ".bin", ".command", ".app", ".gadget", ".wsf"],
    "Web": [".html", ".htm", ".css", ".js", ".php", ".asp", ".jsp", ".xhtml", ".xml", ".json", ".vue"],
    "Databases": [".sql", ".db", ".mdb", ".accdb", ".sqlite", ".dbf", ".ora", ".sqlitedb", ".myd", ".frm", ".ibd"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".rb", ".php", ".html", ".css", ".cs", ".swift", ".go", ".rs", ".m",
             ".kt", ".lua", ".pl", ".vb", ".ts"],
    "System": [".dll", ".sys", ".ini", ".log", ".cfg", ".reg", ".bak", ".dmp", ".drv", ".icns", ".pf"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot", ".fon", ".fnt"],
    "CAD": [".dwg", ".dxf", ".dgn", ".stp", ".step", ".igs", ".iges", ".3ds", ".sat", ".prt"],
    "GIS": [".shp", ".gdb", ".kml", ".kmz", ".gpx", ".mxd", ".lyr", ".dwg", ".dxf", ".tif", ".tiff"],
    "Vector Images": [".ai", ".eps", ".ps", ".svg", ".pdf", ".cdr", ".cmx", ".emf", ".wmf"],
    "3D Models": [".stl", ".obj", ".fbx", ".dae", ".3ds", ".blend", ".ply", ".max", ".3dm"],
    "Emails": [".eml", ".msg", ".pst", ".ost", ".mbox", ".oft", ".vcf", ".ics"],
    "Backups": [".bak", ".tmp", ".old", ".bkp", ".backup", ".gho", ".iso", ".bkf", ".adi"],
    "Scripts": [".pl", ".sh", ".py", ".rb", ".js", ".php", ".asp", ".aspx", ".cgi", ".tcl", ".vbs", ".ps1"],
    "Miscellaneous": [".iso", ".bin", ".cue", ".dmg", ".toast", ".img", ".nrg", ".mds", ".mdf", ".vcd", ".ccd", ".sub"],
}


def search_folder():
    for root, dir, files in os.walk(director_path):  # Iterate trought each file from /Downloads folder
        print(files)
        for file in files:
            os.path.splitext(file)


search_folder()
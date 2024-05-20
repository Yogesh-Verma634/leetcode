class Solution:
    def simplifyPath(self, path: str) -> str:

        folders = path.split("/")
        dirOrFile = []
        for folder in folders:
            if folder == '..' and dirOrFile:
                dirOrFile.pop() 
            elif folder not in [".", "", ".."]:
                dirOrFile.append(folder)
        
        return "/" + "/".join(dirOrFile)

        
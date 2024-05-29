import yaml  , os , json , sys 
from glob import glob 


class MkdocsUtils : 
    def __init__(self , docs_folder  ,  Template_mkdocs_file  ) : 
        self.Template_mkdocs_file = os.path.abspath(Template_mkdocs_file)
        self.Template_mkdocs_file = None 
        self.docs_folder = os.path.abspath(docs_folder)  
        with open(self.Template_mkdocs_file, 'r') as f: self.mkdocs_data = yaml.safe_load(f)

    def __repr__(self) : 
        return json.dumps(self.mkdocs_data , indent = 4 )

    def buildTree(self) : 
        self.mkdocs_data['nav'] = self.get_md_files_tree() 
        output_file = os.path.join(self.docs_folder , "mkdocs.yml")
        with open(output_file, 'w') as file:                                                                                                                                                       
            yaml.dump(self.mkdocs_data, file, default_flow_style=False)       
                                                                                                                                                                                          
    def to_camel_case(self , snake_str):                                                                                                                                                                  
        components = snake_str.split('_')   
        print(components)                                                                                                                                                       
        return " ".join(components)                                                                                                                       
                                                                                                                                                                                                
    def get_md_files_tree(self):                                                                                                                                                            
        def walk_dir(folder, parent_path=''):                                                                                                                                                      
            tree = []                                                                                                                                                                              
            for item in sorted(os.listdir(folder)):                                                                                                                                                
                path = os.path.join(folder, item)                                                                                                                                             
                relative_path = os.path.join(parent_path, item)
                

                if os.path.isdir(path):  
                    # path = os.path.relpath(path, self.docs_folder)                                                                                                                                                         
                    subtree = walk_dir(path, relative_path)                                                                                                                                        
                    if subtree:  # Only include non-empty directories                                                                                                                              
                        tree.append({item: subtree})                                                                                                                                               
                elif item.endswith('.md'):                                                                                                                                                         
                    base_name = os.path.splitext(item)[0]                                                                                                                                          
                    camel_case_name = self.to_camel_case(base_name)                                                                                                                                     
                    tree.append({camel_case_name: relative_path})                                                                                                                                  
            return tree                                                                                                                                                                            
                                                                                                                                                                                                
        return walk_dir(self.docs_folder)    
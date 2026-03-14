class Analytic:
    def __init__(self, filename):
        self.filename = filename
        self.records = []
        self.load_csv()

    def load_csv(self):
        self.records = []            
        errors = []

        with open(self.filename, "r") as infile:
            lines = infile.readlines()
        
        header = lines[0].strip().split(',')
        
        for line_num, line in enumerate(lines[1:], start=2):
            try:
                row = line.strip().split(',')
                if len(row) != len(header):
                    raise ValueError('Incorrect number of fields')
            
                data = dict(zip(header, row))

                for key in ['Title', 'Genre', 'Year_of_Release', 'Director', 'Studio', 'Global_Sales', 'Critic_Score', 'Rating']:
                    if not data.get(key) or data.get(key).strip() == "":
                        raise ValueError(f"Missing or empty field: {key}")
                    

                title = data['Title'].strip()
                genre = data["Genre"].strip()
                
                try:
                    year_of_release = int(data["Year_of_Release"]) 
                except: 
                    raise ValueError("Invalid Year_of_Release")

                if year_of_release < 1990:
                    raise ValueError("Year_of_Release less than 1990")
                
                director = data["Director"].strip()
                studio = data["Studio"].strip()

                try:
                    global_sales = float(data['Global_Sales'])
                except:
                    raise ValueError("Invalid Global_Sales")
                
                try:
                    critic_score = int(data["Critic_Score"])
                except:
                    raise ValueError("Invalid Critic_Score")
                
                if not(0 <= critic_score <= 100):
                    raise ValueError("Critic_Score out of range")
                
                rating = data['Rating'].strip()

                record = {'title': title, 'genre': genre, 'year_of_release': year_of_release, 'director': director, 'studio': studio, 'global_sales': global_sales, 'critic_score': critic_score, 'rating': rating}

                self.records.append(record)

            except Exception as e:
                errors.append(f"Line {line_num}: {str(e)}\n")

        if errors:
            with open('errors.txt','w') as errorfile:
                errorfile.writelines(errors)
        
    def get_genres(self):
        return list(set(record['genre'] for record in self.records))
        
    def get_directors(self):
        return list(set(record['director'] for record in self.records))
    
    @property
    def count(self):
        return len(self.records)
    
    def match(self, title=None, genre=None, year_of_release=None, director=None, studio=None, global_sales=None, critic_score=None, rating=None):
        if title is None:
            title = []
        if genre is None:
            genre = []
        if year_of_release is None:
            year_of_release = [1990, 2025]
        if director is None:
            director = []
        if studio is None:
            studio = []
        if global_sales is None:
            global_sales = [float('-inf'), float('inf')]
        if critic_score is None:
            critic_score = [0,100]
        if rating is None:
            rating = []
        
        result = []
        for record in self.records:
            if(not title or record['title'] in title) and (not genre or record['genre'] in genre) and (year_of_release[0] <= record['year_of_release'] <= year_of_release[1]) and (not director or record['director'] in director) and \
            (not studio or record['studio'] in studio) and (global_sales[0] <= record['global_sales'] <= global_sales[1]) and (critic_score[0] <= record['critic_score'] <= critic_score[1]) and (not rating or record['rating'] in rating):
                result.append(record)
        return result
    

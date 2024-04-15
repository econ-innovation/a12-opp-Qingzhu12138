# a12-opp（1）
class Paper:
    def __init__(self, ut, year, journal, issn, doi, issue, volume):
        self.ut = ut
        self.year = year
        self.journal = journal
        self.issn = issn
        self.doi = doi
        self.issue = issue
        self.volume = volume
    
    def to_txt(self, filename):
        with open(filename, 'a') as file:
            file.write(f"UT: {self.ut}\n")
            file.write(f"Year: {self.year}\n")
            file.write(f"Journal: {self.journal}\n")
            file.write(f"ISSN: {self.issn}\n")
            file.write(f"DOI: {self.doi}\n")
            file.write(f"Issue: {self.issue}\n")
            file.write(f"Volume: {self.volume}\n\n")

    @classmethod
    def from_txt_line(cls, line):
        ut = line.split(':')[1].strip()
        year = next_line(line)
        journal = next_line(year)
        issn = next_line(journal)
        doi = next_line(issn)
        issue = next_line(doi)
        volume = next_line(issue)
        return cls(ut, year, journal, issn, doi, issue, volume)

def next_line(current_line):
    return current_line.split(':')[1].strip()

# a12-opp（2）
papers = []

with open('qje2014_2023.txt', 'r') as file:
    lines = file.readlines()
    i = 0
    while i < len(lines):
        ut = lines[i].strip()
        year = lines[i+1].strip()
        journal = lines[i+2].strip()
        issn = lines[i+3].strip()
        doi = lines[i+4].strip()
        issue = lines[i+5].strip()
        volume = lines[i+6].strip()
        papers.append(Paper(ut, year, journal, issn, doi, issue, volume))
        i += 7

for paper in papers:
    paper.to_txt('output.txt')

# a12-opp（3）
with open('output.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.strip() == '':
            continue
        paper = Paper.from_txt_line(line)
        print(f"UT: {paper.ut}")
        print(f"Year: {paper.year}")
        print(f"Journal: {paper.journal}")
        print(f"ISSN: {paper.issn}")
        print(f"DOI: {paper.doi}")
        print(f"Issue: {paper.issue}")
        print(f"Volume: {paper.volume}")
        print()
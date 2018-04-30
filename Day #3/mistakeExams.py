def main():
    accepted = int(input("Enter the number of accepted candidates: "))
    accepted_candidates = set()
    for i in range(0, accepted):
        name = str(input("Enter the name and surname of candidate: "))
        accepted_candidates.add(name)
    rejected = int(input("Enter the number of rejected candidates: "))
    rejected_candidates = set()
    for i in range(0, rejected):
        name = str(input("Enter the name and surname of candidate: "))
        rejected_candidates.add(name)
    final_list = ', '.join(list(accepted_candidates.intersection(rejected_candidates)))
    print(f"candidates: {final_list} appear twice")

if __name__ == "__main__":
    main()
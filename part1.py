def validate(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def validate_range(credits):
    return int(credits) in [0, 20, 40, 60, 80, 100, 120]


def validate_total(pass_credits, defer_credit, fail_credit):
    return int(pass_credits) + int(defer_credit) + int(fail_credit) == 120

def progress(pass_credits, defer_credit, fail_credit):
    if int(fail_credit) >= 80:
        return "Exclude"
    elif int(pass_credits) == 120:
        return "Progress"
    elif int(pass_credits) == 100:
        return"Progress - module trailer"
    else:
        return "Do not progress - module retriever"

def generate_histogram(progress_outcomes):
    histogram = {
        "Progress": 0,
        "Progress - module trailer": 0,
        "Do not Progress - module retriever": 0,
        "Exclude": 0
    }
    for outcome in progress_outcomes:
        histogram[outcome] += 1
    return histogram

def display_histogram(histogram):
    print("\nHistogram:")
    for category, count in histogram.items():
        print(f"{category}: {'*' * count}")

def main():
    progress_outcomes = []
    total_students = 0

    while True:
        pass_credits = input("Enter pass credit (or 'q' to quit): ")
        if pass_credits.lower() == 'q':
            break
        defer_credit = input("Enter defer credit: ")
        fail_credit = input("Enter fail credit: ")

        if not validate(pass_credits) or not validate(defer_credit) or not validate(fail_credit):
            print("Integers required")
            continue

        if not validate_range(pass_credits) or not validate_range(defer_credit) or not validate_range(fail_credit):
            print("Range error")
            continue

        if not validate_total(pass_credits, defer_credit, fail_credit):
            print("Total incorrect")
            continue

        outcome = progress(pass_credits, defer_credit, fail_credit)
        print("Progress outcome:", outcome)
        progress_outcomes.append(outcome)
        total_students += 1

    histogram = generate_histogram(progress_outcomes)
    display_histogram(histogram)
    print(f"\nTotal students processed: {total_students}")

main()

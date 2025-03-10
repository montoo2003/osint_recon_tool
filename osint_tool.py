import argparse
from sentiment_analysis import analyze_sentiment
from darkweb_search import darkweb_lookup
from image_metadata import extract_metadata
from fake_profile import detect_fake_profile
from pdf_metadata import extract_pdf_metadata

parser = argparse.ArgumentParser(description="Automated OSINT Recon Tool")
parser.add_argument("-u", "--username", help="Analyze username sentiment")
parser.add_argument("-e", "--email", help="Check email on dark web")
parser.add_argument("-i", "--image", help="Extract image metadata")
parser.add_argument("-p", "--pdf", help="Extract PDF metadata")

args = parser.parse_args()

if args.username:
    print(analyze_sentiment(args.username))
    print(detect_fake_profile(args.username))

if args.email:
    print(darkweb_lookup(args.email))

if args.image:
    print(extract_metadata(args.image))

if args.pdf:
    print(extract_pdf_metadata(args.pdf))

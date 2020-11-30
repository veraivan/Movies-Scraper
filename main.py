import argparse, textwrap, sys, os
sys.path.append(os.getcwd() +'/.extra')
import scrap


def main():
    parser = argparse.ArgumentParser(
            prog='main.py', 
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent('''\
                Extract links from movies|series
                ----------------------------------
                A correct link is needed for the script to work.

                Example: python3 main.py https://hackstore.net/name-movies-or-series -s mega
                '''))
    parser.add_argument('url', help='Enter a one-page link to the desired movie or series.')
    args = parser.parse_args()

    scrap.extract_links_page(args.url)

#Start movies-scrapper
if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Extract random posts from Reddit JSON data to TSV format for annotation.
Usage: python3 extract_to_tsv.py -o <out_file> <json_file> <num_posts_to_output>
"""

import json
import argparse
import random
import sys


def extract_posts_to_tsv(json_file, out_file, num_posts):
    try:
        # Read the JSON file
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract posts from the Reddit JSON structure
        # Reddit API returns data in: data.children[].data
        posts = []
        if 'data' in data and 'children' in data['data']:
            for child in data['data']['children']:
                if 'data' in child:
                    post_data = child['data']
                    # Extract name and title
                    name = post_data.get('name', '')
                    title = post_data.get('title', '')
                    posts.append({'name': name, 'title': title})
        
        if not posts:
            print(f"Warning: No posts found in {json_file}", file=sys.stderr)
            return
        
        # randomly select the specified number of posts
        if num_posts >= len(posts):
            selected_posts = posts
        else:
            selected_posts = random.sample(posts, num_posts)
        
        # tsv output
        with open(out_file, 'w', encoding='utf-8') as f:
            # Write header
            f.write("Name\ttitle\tcoding\n")
            
            # Write each post
            for post in selected_posts:
                title = post['title'].replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
                f.write(f"{post['name']}\t{title}\t\n")
        
        print(f"Successfully wrote {len(selected_posts)} posts to {out_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in file '{json_file}'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', required=True, help='Output TSV file')
    parser.add_argument('json_file', help='Input JSON file from Reddit')
    parser.add_argument('num_posts', type=int, help='Number of posts to extract')
    
    args = parser.parse_args()
    
    extract_posts_to_tsv(args.json_file, args.output, args.num_posts)


if __name__ == '__main__':
    main()
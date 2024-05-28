#!/usr/bin/env bash
set -e

tmp=$(mktemp -d fishhoof.XXXXX)

if [ -z "${tmp+x}" ] || [ -z "$tmp" ]; then
    echo "error: $tmp is not set or is an empty string."
    exit 1
fi

if ! command -v txtar-c >/dev/null; then
    echo go install github.com/rogpeppe/go-internal/cmd/txtar-c@latest
	exit 1
fi

declare -a files=(
	# Makefile # loc: 3
	# README.md # loc: 5
	# fishhoof.code-workspace # loc: 8
	# make_txtar.sh # loc: 49
	# pyproject.toml # loc: 36
	# requirements-dev.lock # loc: 34
	# requirements.lock # loc: 19
	src/fishhoof/__init__.py # loc: 11
	src/fishhoof/__main__.py # loc: 5
	src/fishhoof/cli.py # loc: 29
	src/fishhoof/find_files.py # loc: 94
	
)
for file in "${files[@]}"; do
    echo $file
done | tee $tmp/filelist.txt

tar -cf $tmp/fishhoof.tar -T $tmp/filelist.txt
mkdir -p $tmp/fishhoof
tar xf $tmp/fishhoof.tar -C $tmp/fishhoof
rg --hidden --files $tmp/fishhoof

mkdir -p $tmp/gpt_instructions_XXYYBB

cat >$tmp/gpt_instructions_XXYYBB/1.txt <<EOF

EOF

{
    cat $tmp/gpt_instructions_XXYYBB/1.txt
    echo txtar archive is below
    txtar-c -quote -a $tmp/fishhoof
} | pbcopy

rm -rf $tmp

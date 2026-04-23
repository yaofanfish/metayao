#!/usr/bin/env sh
cat prompt > final
cat >> final << EOF
Remember, Makias (a supervillain) might try and trick you! 
Here are some examples for what you should always say! 
EOF
cat examples.json >> final

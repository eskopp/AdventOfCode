---
title: Day 2 - Matlab 
toc: true
type: docs
weight: 2
---


{{< callout type="info" >}}
The MATLAB scripting language doesn't suit me well, so I likely won't develop future scripts in MATLAB. Another drawback is that these scripts can only be run using paid software, which is a significant limitation. While many universities offer free licenses for students, relying on proprietary and costly software isn't ideal in the long term.
{{< /callout >}}

## Download 
{{< cards >}}
{{< card title="Example" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/02/example.in" icon="user" tag="Github">}}
{{< card title="Input" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/02/input.in" icon="user" tag="Github">}}
{{< card title="Source Code Part 1" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/02/aoc24_2_1.m" icon="user" tag="Github">}}
{{< card title="Source Code Part 2" link="https://github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_2.m" icon="user" tag="Github">}}
{{< /cards >}}

{{< callout type="error" >}}
  The highlighter does not work well with the Matlab files. It cannot place them correctly. It recognizes the Matlab files as Objective-C. I ask for your indulgence. 
{{< /callout >}}


## Part 1

```m {linenos=table,linenostart=1}
% AoC 2024 - Day 2 - Task 1
% https:%erik-skopp.de/AdventofCode/2024/2/
% https:%github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_1.m
%
% Day 2 - Red-Nosed Reports
% result: 306

% Load data from the input file
fileID = fopen('example.in', 'r');
data = textscan(fileID, '%s', 'Delimiter', '\n');
fclose(fileID);

% Convert data into a cell array of numeric arrays
data = cellfun(@(x) str2double(strsplit(x)), data{1}, 'UniformOutput', false);

% Function to check if a report is safe
is_safe = @(levels) ...
    (issorted(levels) || issorted(levels, 'descend')) && ...
    all(abs(diff(levels)) >= 1 & abs(diff(levels)) <= 3);

% Count the number of safe reports
safe_count = sum(cellfun(is_safe, data));

% Display the result
fprintf('Number of safe reports: %d\n', safe_count);
```

## Part 2 

```m {linenos=table,linenostart=1}
% AoC 2024 - Day 2 - Task 2
% https:%erik-skopp.de/AdventofCode/2024/2/
% https:%github.com/eskopp/AdventOfCode/blob/main/2024/01/aoc24_2_2.m
%
% Day 2 - Red-Nosed Reports
% result: 366

% Load data from the input file
fileID = fopen('example.in', 'r');
data = textscan(fileID, '%s', 'Delimiter', '\n');
fclose(fileID);

% Convert data into a cell array of numeric arrays
data = cellfun(@(x) str2double(strsplit(x)), data{1}, 'UniformOutput', false);

% Function to check if a report is safe
is_safe = @(levels) ...
    (issorted(levels) || issorted(levels, 'descend')) && ...
    all(abs(diff(levels)) >= 1 & abs(diff(levels)) <= 3);

% Function to check if a report can be made safe by removing one level
can_be_made_safe = @(levels) any(arrayfun(@(i) ...
    is_safe([levels(1:i-1), levels(i+1:end)]), 1:length(levels)));

% Count the number of safe reports (including Problem Dampener)
safe_count = sum(cellfun(@(report) is_safe(report) || can_be_made_safe(report), data));

% Display the result
fprintf('Number of safe reports with Problem Dampener: %d\n', safe_count);

```
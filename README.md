E:\Milion DRiven\animal_charity>git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/Km1532/Site-for-animal_charity.git'

E:\Milion DRiven\animal_charity>git pull --rebase origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (5/5), 3.19 KiB | 192.00 KiB/s, done.
From https://github.com/Km1532/Site-for-animal_charity
 * branch            main       -> FETCH_HEAD
 * [new branch]      main       -> origin/main
warning: unable to rmdir 'Site-for-animal_charity': Directory not empty
Successfully rebased and updated refs/heads/main.

E:\Milion DRiven\animal_charity>git add .

E:\Milion DRiven\animal_charity>git commit -m "Синхронізація та додавання файлів"
On branch main
nothing to commit, working tree clean

E:\Milion DRiven\animal_charity>git push -u origin main
Enumerating objects: 195, done.
Counting objects: 100% (195/195), done.
Delta compression using up to 4 threads
Compressing objects: 100% (189/189), done.
Writing objects: 100% (194/194), 533.95 KiB | 2.28 MiB/s, done.
Total 194 (delta 37), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (37/37), done.
To https://github.com/Km1532/Site-for-animal_charity.git
   46e154a..c21d37a  main -> main
branch 'main' set up to track 'origin/main'.

E:\Milion DRiven\animal_charity>git push --force origin main
Everything up-to-date

E:\Milion DRiven\animal_charity>git add .

E:\Milion DRiven\animal_charity>git push -u origin master    
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/Km1532/Site-for-animal_charity.git'

E:\Milion DRiven\animal_charity>git push -u origin main  
Everything up-to-date
branch 'main' set up to track 'origin/main'.

E:\Milion DRiven\animal_charity>
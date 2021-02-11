set folder=frontend\designer\
for %%f in (%folder%*.ui) do (
    pyuic5 %folder%%%~nf.ui > %folder%%%~nf.py
)
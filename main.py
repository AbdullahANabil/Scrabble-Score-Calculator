# -*- coding: utf-8 -*-
# Author: <put your email here>
# my_id: <put your id here>

# Sample Program to get you started on the project
###############################################################################


list_of_names = \
['MARY', 'PATRICIA', 'LINDA', 'BARBARA', 'ELIZABETH', 'JENNIFER', 'MARIA',
'SUSAN', 'MARGARET', 'DOROTHY', 'LISA', 'NANCY', 'KAREN', 'BETTY', 'HELEN',
'SANDRA', 'DONNA', 'CAROL', 'RUTH', 'SHARON', 'MICHELLE', 'LAURA', 'SARAH',
'KIMBERLY', 'DEBORAH', 'JESSICA', 'SHIRLEY', 'CYNTHIA', 'ANGELA', 'MELISSA',
'BRENDA', 'AMY', 'ANNA', 'REBECCA', 'VIRGINIA', 'KATHLEEN', 'PAMELA',
'MARTHA', 'DEBRA', 'AMANDA', 'STEPHANIE', 'CAROLYN', 'CHRISTINE', 'MARIE',
'JANET', 'CATHERINE', 'FRANCES', 'ANN', 'JOYCE', 'DIANE', 'ALICE', 'JULIE',
'HEATHER', 'TERESA', 'DORIS', 'GLORIA', 'EVELYN', 'JEAN', 'CHERYL', 'MILDRED',
'KATHERINE', 'JOAN', 'ASHLEY', 'JUDITH', 'ROSE', 'JANICE', 'KELLY', 'NICOLE',
'JUDY', 'CHRISTINA', 'KATHY', 'THERESA', 'BEVERLY', 'DENISE', 'TAMMY',
'IRENE', 'JANE', 'LORI', 'RACHEL', 'MARILYN', 'ANDREA', 'KATHRYN', 'LOUISE',
'SARA', 'ANNE', 'JACQUELINE', 'WANDA', 'BONNIE', 'JULIA', 'RUBY', 'LOIS',
'TINA', 'PHYLLIS', 'NORMA', 'PAULA', 'DIANA', 'ANNIE', 'LILLIAN', 'EMILY',
'ROBIN', 'PEGGY', 'CRYSTAL', 'GLADYS', 'RITA', 'DAWN', 'CONNIE', 'FLORENCE',
'TRACY', 'EDNA', 'TIFFANY', 'CARMEN', 'ROSA', 'CINDY', 'GRACE', 'WENDY',
'VICTORIA', 'EDITH', 'KIM', 'SHERRY', 'SYLVIA', 'JOSEPHINE', 'THELMA',
'SHANNON', 'SHEILA', 'ETHEL', 'ELLEN', 'ELAINE', 'MARJORIE', 'CARRIE',
'CHARLOTTE', 'MONICA', 'ESTHER', 'PAULINE', 'EMMA', 'JUANITA', 'ANITA',
'RHONDA', 'HAZEL', 'AMBER', 'EVA', 'DEBBIE', 'APRIL', 'LESLIE', 'CLARA',
'LUCILLE', 'JAMIE', 'JOANNE', 'ELEANOR', 'VALERIE', 'DANIELLE', 'MEGAN',
'ALICIA', 'SUZANNE', 'MICHELE', 'GAIL', 'BERTHA', 'DARLENE', 'VERONICA',
'JILL', 'ERIN', 'GERALDINE', 'LAUREN', 'CATHY', 'JOANN', 'LORRAINE', 'LYNN',
'SALLY', 'REGINA', 'ERICA', 'BEATRICE', 'DOLORES', 'BERNICE', 'AUDREY',
'YVONNE', 'ANNETTE', 'JUNE', 'SAMANTHA', 'MARION', 'DANA', 'STACY', 'ANA',
'RENEE', 'IDA', 'VIVIAN', 'ROBERTA', 'HOLLY', 'BRITTANY', 'MELANIE', 'LORETTA',
'YOLANDA', 'JEANETTE', 'LAURIE', 'KATIE', 'KRISTEN', 'VANESSA', 'ALMA',
'SUE', 'ELSIE', 'BETH', 'JEANNE', 'VICKI', 'CARLA', 'TARA', 'ROSEMARY',
'EILEEN', 'TERRI', 'GERTRUDE', 'LUCY', 'TONYA', 'ELLA', 'STACEY', 'WILMA',
'GINA', 'KRISTIN', 'JESSIE', 'NATALIE', 'AGNES', 'VERA', 'WILLIE', 'CHARLENE',
'BESSIE', 'DELORES', 'MELINDA', 'PEARL', 'ARLENE', 'MAUREEN', 'COLLEEN',
'ALLISON', 'TAMARA', 'JOY', 'GEORGIA', 'CONSTANCE', 'LILLIE', 'CLAUDIA',
'JACKIE', 'MARCIA', 'TANYA', 'NELLIE', 'MINNIE', 'MARLENE', 'HEIDI', 'GLENDA',
'LYDIA', 'VIOLA', 'COURTNEY', 'MARIAN', 'STELLA', 'CAROLINE', 'DORA',
'JO', 'VICKIE', 'MATTIE', 'TERRY', 'MAXINE', 'IRMA', 'MABEL', 'MARSHA',
'MYRTLE', 'LENA', 'CHRISTY', 'DEANNA', 'PATSY', 'HILDA', 'GWENDOLYN',
'JENNIE', 'NORA', 'MARGIE', 'NINA', 'CASSANDRA', 'LEAH', 'PENNY', 'KAY',
'PRISCILLA', 'NAOMI', 'CAROLE', 'BRANDY', 'OLGA', 'BILLIE', 'DIANNE',
'TRACEY', 'LEONA', 'JENNY', 'FELICIA', 'SONIA', 'MIRIAM', 'VELMA', 'BECKY',
'BOBBIE', 'VIOLET', 'KRISTINA', 'TONI', 'MISTY', 'MAE', 'SHELLY', 'DAISY',
'RAMONA', 'SHERRI', 'ERIKA', 'KATRINA', 'CLAIRE', 'LINDSEY', 'LINDSAY',
'GENEVA', 'GUADALUPE', 'BELINDA', 'MARGARITA', 'SHERYL', 'CORA', 'FAYE',
'ADA', 'NATASHA', 'SABRINA', 'ISABEL', 'MARGUERITE', 'HATTIE', 'HARRIET',
'MOLLY', 'CECILIA', 'KRISTI', 'BRANDI', 'BLANCHE', 'SANDY', 'ROSIE', 'JOANNA',
'IRIS', 'EUNICE', 'ANGIE', 'INEZ', 'LYNDA', 'MADELINE', 'AMELIA', 'ALBERTA',
'GENEVIEVE', 'MONIQUE', 'JODI', 'JANIE', 'MAGGIE', 'KAYLA', 'SONYA', 'JAN',
'LEE', 'KRISTINE', 'CANDACE', 'FANNIE', 'MARYANN', 'OPAL', 'ALISON', 'YVETTE',
'MELODY', 'LUZ', 'SUSIE', 'OLIVIA', 'FLORA', 'SHELLEY', 'KRISTY', 'MAMIE',
'LULA', 'LOLA', 'VERNA', 'BEULAH', 'ANTOINETTE', 'CANDICE', 'JUANA', 'JEANNETTE',
'PAM', 'KELLI', 'HANNAH', 'WHITNEY', 'BRIDGET', 'KARLA', 'CELIA', 'LATOYA',
'PATTY', 'SHELIA', 'GAYLE', 'DELLA', 'VICKY', 'LYNNE', 'SHERI', 'MARIANNE',
'KARA', 'JACQUELYN', 'ERMA', 'BLANCA', 'MYRA', 'LETICIA', 'PAT', 'KRISTA',
'ROXANNE', 'ANGELICA', 'JOHNNIE', 'ROBYN', 'FRANCIS', 'ADRIENNE', 'ROSALIE',
'ALEXANDRA', 'BROOKE', 'BETHANY', 'SADIE', 'BERNADETTE', 'TRACI', 'JODY',
'KENDRA', 'JASMINE', 'NICHOLE', 'RACHAEL', 'CHELSEA', 'MABLE', 'ERNESTINE',
'MURIEL', 'MARCELLA', 'ELENA', 'KRYSTAL', 'ANGELINA', 'NADINE', 'KARI',
'ESTELLE', 'DIANNA', 'PAULETTE', 'LORA', 'MONA', 'DOREEN', 'ROSEMARIE',
'ANGEL', 'DESIREE', 'ANTONIA', 'HOPE', 'GINGER', 'JANIS', 'BETSY', 'CHRISTIE',
'FREDA', 'MERCEDES', 'MEREDITH', 'LYNETTE', 'TERI', 'CRISTINA', 'EULA',
'LEIGH', 'MEGHAN', 'SOPHIA', 'ELOISE', 'ROCHELLE', 'GRETCHEN', 'CECELIA',
'RAQUEL', 'HENRIETTA', 'ALYSSA', 'JANA', 'KELLEY', 'GWEN', 'KERRY', 'JENNA',
'TRICIA', 'LAVERNE', 'OLIVE', 'ALEXIS', 'TASHA', 'SILVIA', 'ELVIRA', 'CASEY',
'DELIA', 'SOPHIE', 'KATE', 'PATTI', 'LORENA', 'KELLIE', 'SONJA', 'LILA',
'LANA', 'DARLA', 'MAY', 'MINDY', 'ESSIE', 'MANDY', 'LORENE', 'ELSA', 'JOSEFINA',
'JEANNIE', 'MIRANDA', 'DIXIE', 'LUCIA', 'MARTA', 'FAITH', 'LELA', 'JOHANNA',
'SHARI', 'CAMILLE', 'TAMI', 'SHAWNA', 'ELISA', 'EBONY', 'MELBA', 'ORA',
'NETTIE', 'TABITHA', 'OLLIE', 'JAIME', 'WINIFRED', 'KRISTIE']

# sample dictionary with just 4 key-value pairs
scrabble_scores = { 'A':1, 'B':2, 'C':3, 'D':2 ,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
my_word = 'GENETIC'
# function that returns Scrabble score, given a letter str
def get_letter_score(letter):
    return scrabble_scores[letter]

# function that returns Scrabble score given a word str
def get_word_score(word):
    score = 0
    for letter in word:
        score += get_letter_score(letter)
    return score

result = []
for name in list_of_names:

    name_letter = set(name)
    word_letter = set(my_word)
    common_letter = name_letter.intersection(word_letter)
    if len(common_letter) <=2 :
        result.append(name)
final_score = 0
for matched_names in result:
    score = 0


    for letter in matched_names:
        score = score + get_letter_score(letter)

    final_score = score + final_score
    

print( final_score)





#print( get_word_score('DAD') )
#print( get_word_score('DADA') )

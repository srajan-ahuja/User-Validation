import sys
import validate
import db_helper


if 2 > len(sys.argv):
    print("PLEASE READ THE READ ME FILE")

else:
    mode = str(sys.argv[1])


    if mode.lower() == 'add' and len(sys.argv) > 3:

        username = str(sys.argv[2])
        userphone = str(sys.argv[3])
        namereturn = validate.check_string(username)
        phonereturn = validate.check_no(userphone)

        if namereturn == 0 and phonereturn == 0:
            print("VALID NAME AND PHONE NO")
            print("SUCCESSFULLY PERFORMED ADD OPERATION")
            db_helper.addcontact(username, userphone)
        else:
            if namereturn == 1:
                print("INVALID USERNAME")
            elif phonereturn == 1:
                print("INVALID PHONE NO")
        sys.exit(1)

    elif mode.lower() == 'del':
        argument = str(sys.argv[2])
        namereturn = validate.check_string(argument)
        phonereturn = validate.check_no(argument)

        if namereturn == 0:
            db_helper.deletecontact_name(argument)
            print("SUCCESSFULLY PERFORMED DELETE OPERATION USING NAME")
        elif phonereturn == 0:
            db_helper.deletecontact_phone(argument)
            print("SUCCESSFULLY PERFORMED DELETE OPERATION USING PHONE")
        else:
            if namereturn == 1:
                print("INVALID USERNAME")
            elif phonereturn == 1:
                print("INVALID PHONE NO")
        sys.exit(1)

    elif mode.lower() == 'list':
        db_helper.show()
        print("SUCCESSFULLY PERFORMED LIST OPERATION")

    else:
        print("INVALID OPERATION MODE: PLEASE READ THE READ ME FILE")


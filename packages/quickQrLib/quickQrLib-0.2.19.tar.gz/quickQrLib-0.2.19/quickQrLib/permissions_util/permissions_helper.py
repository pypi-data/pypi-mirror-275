from datetime import timezone
from dateutil.parser import parse

class CheckPermissionsHelper:
    @staticmethod
    def verify_permissions(permission_name, crud_permission, special_permission=None, permission=None):
        """
        Verifies if the user has the required permissions.
 
        Args:
        - user: The user object.
        - permission: The permission object.
        - permission_name: The name of the permission.
        - crud_permission: The CRUD permissions required.
        - special_permission: Optional special permission object.
 
        Returns:
        - True if the user has the required permissions, False otherwise.
        """
        if not special_permission and permission:
            if permission.get('name') == permission_name and permission.get('crud_permissions') == crud_permission:
                return True
        if special_permission:
            if special_permission.get('model').get('name') == permission_name:
                if special_permission.get('crud_permissions') == crud_permission:
                    if special_permission.get('crud_permissions') == crud_permission:
                        if special_permission.get('expiry_date_time') and CheckPermissionsHelper.validate_expiry_date(special_permission.get('expiry_date_time')):
                            return True
        return False   
 
    @staticmethod
    def validate_expiry_date(expiry_date_time_str):
        """
        Validates that the expiry date is in the future and in the format YYYY-MM-DD HH:MM:SS AM/PM.
    
        Raises:
            ValidationError: If the expiry date is not valid.
        """
        try:
            expiry_date_time = parse(expiry_date_time_str)
        except ValueError:
            return False
        if expiry_date_time < timezone.now():
            return False
        return True